from fastapi import FastAPI, HTTPException
from model import (
    Aragami, AragamiCreate,
    GodArc, GodArcCreate,
    GodEater, GodEaterCreate,
)

app = FastAPI()


@app.get("/aragami", response_model=list[Aragami], tags=["Aragami"])
def listar_aragami():
    return aragami_db.get_all()


@app.get("/aragami/{aragami_id}", response_model=Aragami, tags=["Aragami"])
def obtener_aragami(aragami_id: int):
    obj = aragami_db.get_by_id(aragami_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Aragami no encontrado")
    return obj