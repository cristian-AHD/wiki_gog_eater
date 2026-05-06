from fastapi import FastAPI, HTTPException
from Crud import CRUDCSV, Historial
from model import (
    Aragami, AragamiCreate,
    GodArc, GodArcCreate,
    GodEater, GodEaterCreate
)

app = FastAPI()

aragami_db = CRUDCSV("aragami.csv")
godarc_db  = CRUDCSV("godarc.csv")
godeater_db = CRUDCSV("godeater.csv")

historial = Historial()

@app.get("/aragami")
def listar_aragami():
    return list(aragami_db)

@app.get("/aragami/{id}")
def buscar_aragami(id: int):
    for x in aragami_db:
        if int(x["id"]) == id:
            return x
    raise HTTPException(404, "Aragami no encontrado")


@app.post("/aragami")
def crear_aragami(data: AragamiCreate):
    nuevo = Aragami(
        id=len(aragami_db) + 1,
        nombre=data.nombre,
        tipo=data.tipo,
        debilidades=data.debilidades,
        descripcion=data.descripcion,
    )
    aragami_db.append(nuevo)
    return nuevo


@app.put("/aragami/{id}")
def actualizar_aragami(id: int, data: AragamiCreate):
    for i, x in enumerate(aragami_db):
        if int(x["id"]) == id:
            actualizado = Aragami(
                id=id,
                nombre=data.nombre,
                tipo=data.tipo,
                debilidades=data.debilidades,
                descripcion=data.descripcion,
            )
            aragami_db[i] = actualizado
            return actualizado
    raise HTTPException(404, "Aragami no encontrado")


@app.delete("/aragami/{id}")
def eliminar_aragami(id: int):
    for i, x in enumerate(aragami_db):
        if int(x["id"]) == id:
            # Guardar en historial antes de eliminar
            nombre = x.get("nombre", "Desconocido")
            historial.registrar("Aragami", id, nombre)

            aragami_db.delete(i)
            return {"mensaje": "Aragami eliminado", "id_eliminado": id, "nombre": nombre}
    raise HTTPException(404, "Aragami no encontrado")

@app.get("/aragami/nombre/{nombre}")
def buscar_por_nombre(nombre: str):
    return [x for x in aragami_db if x["nombre"].lower() == nombre.lower()]

@app.get("/aragami/elemento/{elemento}")
def filtrar_por_elemento(elemento: str):
    elemento = elemento.capitalize()
    return [x for x in aragami_db if elemento in x.get("debilidades", [])]


@app.get("/godarc")
def listar_godarc():
    return list(godarc_db)

@app.get("/godarc/{id}")
def buscar_godarc(id: int):
    for x in godarc_db:
        if int(x["id"]) == id:
            return x
    raise HTTPException(404, "GodArc no encontrado")

@app.post("/godarc")
def crear_godarc(data: GodArcCreate):
    nuevo = GodArc(
        id=len(godarc_db) + 1,
        nombre=data.nombre,
        espada=data.espada,
        escudo=data.escudo,
        pistola=data.pistola,
        unidad_control=data.unidad_control,
        descripcion=data.descripcion,
    )
    godarc_db.append(nuevo)
    return nuevo

@app.put("/godarc/{id}")
def actualizar_godarc(id: int, data: GodArcCreate):
    for i, x in enumerate(godarc_db):
        if int(x["id"]) == id:
            actualizado = GodArc(
                id=id,
                nombre=data.nombre,
                espada=data.espada,
                escudo=data.escudo,
                pistola=data.pistola,
                unidad_control=data.unidad_control,
                descripcion=data.descripcion,
            )
            godarc_db[i] = actualizado
            return actualizado
    raise HTTPException(404, "GodArc no encontrado")


@app.delete("/godarc/{id}")
def eliminar_godarc(id: int):
    for i, x in enumerate(godarc_db):
        if int(x["id"]) == id:
            # Guardar en historial antes de eliminar
            nombre = x.get("nombre", "Desconocido")
            historial.registrar("GodArc", id, nombre)

            godarc_db.delete(i)
            return {"mensaje": "GodArc eliminado", "id_eliminado": id, "nombre": nombre}
    raise HTTPException(404, "GodArc no encontrado")


@app.get("/godeater")
def listar_godeater():
    return list(godeater_db)


@app.get("/godeater/{id}")
def buscar_godeater(id: int):
    for x in godeater_db:
        if int(x["id"]) == id:
            return x
    raise HTTPException(404, "GodEater no encontrado")


@app.post("/godeater")
def crear_godeater(data: GodEaterCreate):
    if data.god_arc_id is not None:
        existe = any(int(g["id"]) == data.god_arc_id for g in godarc_db)
        if not existe:
            raise HTTPException(404, "GodArc relacionado no existe")

    nuevo = GodEater(
        id=len(godeater_db) + 1,
        nombre=data.nombre,
        rango=data.rango,
        god_arc_id=data.god_arc_id,
        descripcion=data.descripcion,
    )
    godeater_db.append(nuevo)
    return nuevo


@app.put("/godeater/{id}")
def actualizar_godeater(id: int, data: GodEaterCreate):
    for i, x in enumerate(godeater_db):
        if int(x["id"]) == id:
            if data.god_arc_id is not None:
                existe = any(int(g["id"]) == data.god_arc_id for g in godarc_db)
                if not existe:
                    raise HTTPException(404, "GodArc relacionado no existe")
            actualizado = GodEater(
                id=id,
                nombre=data.nombre,
                rango=data.rango,
                god_arc_id=data.god_arc_id,
                descripcion=data.descripcion,
            )
            godeater_db[i] = actualizado
            return actualizado
    raise HTTPException(404, "GodEater no encontrado")


@app.delete("/godeater/{id}")
def eliminar_godeater(id: int):
    for i, x in enumerate(godeater_db):
        if int(x["id"]) == id:
            nombre = x.get("nombre", "Desconocido")
            historial.registrar("GodEater", id, nombre)

            godeater_db.delete(i)
            return {"mensaje": "GodEater eliminado", "id_eliminado": id, "nombre": nombre}
    raise HTTPException(404, "GodEater no encontrado")


@app.get("/godeater/rango/{rango}")
def filtrar_rango(rango: str):
    return [x for x in godeater_db if x["rango"].lower() == rango.lower()]


@app.get("/historial")
def ver_historial():
    return historial.obtener_todos()

@app.get("/historial/{tipo}")
def ver_historial_por_tipo(tipo: str):
    tipos_validos = ["Aragami", "GodArc", "GodEater"]
    if tipo not in tipos_validos:
        raise HTTPException(400, f"Tipo inválido. Use: {tipos_validos}")

    resultado = historial.obtener_por_tipo(tipo)
    return resultado

@app.delete("/historial/limpiar")
def limpiar_historial():
    historial.limpiar()
    return {"mensaje": "Historial limpiado exitosamente"}

@app.get("/historial/cantidad")
def cantidad_historial():
    return {"total_registros": len(historial)}