from fastapi import FastAPI, HTTPException
from model import (
    Aragami, AragamiCreate,
    GodArc, GodArcCreate,
    GodEater, GodEaterCreate
)

app = FastAPI()


aragami_db = []
godarc_db = []
godeater_db = []

@app.get("/aragami")
def listar_aragami():
    return [x for x in aragami_db if x.estado == "Activo"]


@app.get("/aragami/{id}")
def obtener_aragami(id: int):
    for x in aragami_db:
        if x.id == id:
            return x
    raise HTTPException(404, "Aragami no encontrado")

@app.post("/aragami")
def crear_aragami(data: AragamiCreate):
    nuevo = Aragami(
        id=len(aragami_db) + 1,
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
        if x.id == id:
            aragami_db[i] = Aragami(
                id=id,
                nombre=data.nombre,
                tipo=data.tipo,
                elemento=data.elemento,
                debilidades=data.debilidades,
                descripcion=data.descripcion,
                estado="Activo"
            )
            return aragami_db[i]
    raise HTTPException(404, "Aragami no encontrado")

@app.delete("/aragami/{id}")
def eliminar_aragami(id: int):
    for x in aragami_db:
        if x.id == id:
            x.estado = "Inactivo"
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
        descripcion=data.descripcion,
        estado="Activo"
    )
    godarc_db.append(nuevo)
    return nuevo

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
        descripcion=data.descripcion,
        estado="Activo"
    )
    godarc_db.append(nuevo)
    return nuevo


@app.delete("/godarc/{id}")
def eliminar_godarc(id: int):
    for x in godarc_db:
        if x.id == id:
            x.estado = "Inactivo"
            return {"mensaje": "GodArc inactivado"}
    raise HTTPException(404, "GodArc no encontrado")


