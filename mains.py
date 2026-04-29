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


