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


@app.get("/aragami/{aragami_id}", response_model=Aragami, tags=["Aragami"])
def obtener_aragami(aragami_id: int):
    obj = aragami_db.get_by_id(aragami_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Aragami no encontrado")
    return obj