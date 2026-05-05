from fastapi import FastAPI, HTTPException
from Crud import CRUDCSV
from model import (
    Aragami, AragamiCreate,
    GodArc, GodArcCreate,
    GodEater, GodEaterCreate
)

app = FastAPI()

aragami_db = CRUDCSV("aragami.csv")
godarc_db  = CRUDCSV("godarc.csv")
godeater_db = CRUDCSV("godeater.csv")

@app.get("/aragami")
def lista_aragami():
    return [x for x in aragami_db if x["estado"] == "Activo"]

@app.get("/aragami/{id}")
def Buscar_aragami(id: int):
    for x in CRUDCSV("aragami.csv"):
        if x.id == id:
            return x
    raise HTTPException(404, "Aragami no encontrado")

@app.post("/aragami")
def crear_aragami(data: AragamiCreate):
    nuevo = Aragami(
        id=len(CRUDCSV("aragami.csv")) + 1,
        nombre=data.nombre,
        tipo=data.tipo,
        elemento=data.elemento,
        debilidades=data.debilidades,
        descripcion=data.descripcion,
        estado="Activo"
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
                elemento=data.elemento,
                debilidades=data.debilidades,
                descripcion=data.descripcion,
                estado=x["estado"]
            )
            aragami_db[i] = actualizado
            return actualizado
    raise HTTPException(404, "Aragami no encontrado")

@app.delete("/aragami/{id}")
def eliminar_aragami(id: int):
    for i, x in enumerate(aragami_db):
        if int(x["id"]) == id:
            x["estado"] = "Inactivo"
            aragami_db.save()
            return {"mensaje": "Aragami inactivado"}
    raise HTTPException(404, "Aragami no encontrado")

@app.get("/aragami/nombre/{nombre}")
def buscar_nombre(nombre: str):
    return [x for x in aragami_db if x.nombre.lower() == nombre.lower()]


@app.get("/aragami/elemento/{elemento}")
def filtrar_elemento(elemento: str):
    return [x for x in aragami_db if x.elemento == elemento]

@app.get("/godarc")
def listar_godarc():
    return [x for x in godarc_db if x.estado == "Activo"]


@app.post("/godarc")
def crear_godarc(data: GodArcCreate):
    nuevo = GodArc(
        id=len(godarc_db) + 1,
        nombre=data.nombre,
        tipo_hoja=data.tipo_hoja,
        tipo_disparo=data.tipo_disparo,
        elemento=data.elemento,
        estado="Activo"
    )
    godarc_db.append(nuevo)
    return nuevo

@app.delete("/godarc/{id}")
def eliminar_godarc(id: int):
    for i, x in enumerate(godarc_db):
        if int(x["id"]) == id:
            x["estado"] = "Inactivo"
            godarc_db.save()
            return {"mensaje": "GodArc inactivado"}
    raise HTTPException(404, "GodArc no encontrado")

@app.get("/godeater")
def listar_godeater():
    return [x for x in godeater_db if x.estado == "Activo"]


@app.post("/godeater")
def crear_godeater(data: GodEaterCreate):

    if data.god_arc_id is not None:
        existe = False
        for g in godarc_db:
            if g.id == data.god_arc_id:
                existe = True

        if not existe:
            raise HTTPException(404, "GodArc relacionado no existe")

    nuevo = GodEater(
        id=len(godeater_db) + 1,
        nombre=data.nombre,
        rango=data.rango,
        god_arc_id=data.god_arc_id,
        descripcion=data.descripcion,
        estado="Activo"
    )
    godeater_db.append(nuevo)
    return nuevo

@app.get("/godeater/rango/{rango}")
def filtrar_rango(rango: str):
    return [x for x in godeater_db if x.rango.lower() == rango.lower()]

@app.delete("/godeater/{id}")
def eliminar_godeater(id: int):
    for i, x in enumerate(godeater_db):
        if int(x["id"]) == id:
            x["estado"] = "Inactivo"
            godeater_db.save()
            return {"mensaje": "GodEater inactivado"}
    raise HTTPException(404, "GodEater no encontrado")