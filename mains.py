from fastapi import FastAPI, HTTPException, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel as PydanticBase
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from Batabase import get_db, engine
import Models_db
from model import (
    Aragami, AragamiCreate,
    Espada, EspadaCreate,
    Escudo, EscudoCreate,
    Pistola, PistolaCreate,
    UnidadControl, UnidadControlCreate,
    GodEater, GodEaterCreate,
    Material, MaterialCreate,
    Area, AreaCreate
)

Models_db.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return FileResponse("estilo_god/index.html", media_type="text/html")

app.mount("/", StaticFiles(directory="estilo_god"), name="static")

# ── ARAGAMI ──────────────────────────────────────────────────────────────────

@app.get("/api/aragami")
def listar_aragami(db: Session = Depends(get_db)):
    return db.query(Models_db.AragamiDB).all()


@app.get("/api/aragami/nombre/{nombre}")
def buscar_aragami_nombre(nombre: str, db: Session = Depends(get_db)):
    return db.query(Models_db.AragamiDB).filter(
        Models_db.AragamiDB.nombre.ilike(f"%{nombre}%")
    ).all()


@app.get("/api/aragami/{id}")
def buscar_aragami(id: int, db: Session = Depends(get_db)):
    aragami = db.query(Models_db.AragamiDB).filter(Models_db.AragamiDB.id == id).first()
    if not aragami:
        raise HTTPException(404, "Aragami no encontrado")
    return aragami


@app.post("/api/aragami")
def crear_aragami(data: AragamiCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.AragamiDB(
        nombre=data.nombre,
        tipo=data.tipo,
        debilidades=data.debilidades,
        descripcion=data.descripcion,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.put("/api/aragami/{id}")
def actualizar_aragami(id: int, data: AragamiCreate, db: Session = Depends(get_db)):
    aragami = db.query(Models_db.AragamiDB).filter(Models_db.AragamiDB.id == id).first()
    if not aragami:
        raise HTTPException(404, "Aragami no encontrado")
    aragami.nombre = data.nombre
    aragami.tipo = data.tipo
    aragami.debilidades = data.debilidades
    aragami.descripcion = data.descripcion
    db.commit()
    db.refresh(aragami)
    return aragami


@app.delete("/api/aragami/{id}")
def eliminar_aragami(id: int, db: Session = Depends(get_db)):
    aragami = db.query(Models_db.AragamiDB).filter(Models_db.AragamiDB.id == id).first()
    if not aragami:
        raise HTTPException(404, "Aragami no encontrado")
    db.delete(aragami)
    db.commit()
    return {"mensaje": "Aragami eliminado", "id": id, "nombre": aragami.nombre}


# ── ESPADA ──────────────────────────────────────────────────────────────────

@app.get("/api/espada")
def listar_espadas(db: Session = Depends(get_db)):
    return db.query(Models_db.EspadaDB).all()


@app.get("/api/espada/tipo/{tipo}")
def filtrar_espada_tipo(tipo: str, db: Session = Depends(get_db)):
    return db.query(Models_db.EspadaDB).filter(
        Models_db.EspadaDB.tipo.ilike(tipo)
    ).all()


@app.get("/api/espada/{id}")
def buscar_espada(id: int, db: Session = Depends(get_db)):
    espada = db.query(Models_db.EspadaDB).filter(Models_db.EspadaDB.id == id).first()
    if not espada:
        raise HTTPException(404, "Espada no encontrada")
    return espada


@app.post("/api/espada")
def crear_espada(data: EspadaCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.EspadaDB(
        nombre=data.nombre,
        tipo=data.tipo,
        elemento=data.elemento,
        sunder=data.sunder,
        crush=data.crush,
        pierce=data.pierce,
        valor_elemento=data.valor_elemento,
        materiales=data.materiales,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.put("/api/espada/{id}")
def actualizar_espada(id: int, data: EspadaCreate, db: Session = Depends(get_db)):
    espada = db.query(Models_db.EspadaDB).filter(Models_db.EspadaDB.id == id).first()
    if not espada:
        raise HTTPException(404, "Espada no encontrada")
    espada.nombre = data.nombre
    espada.tipo = data.tipo
    espada.elemento = data.elemento
    espada.sunder = data.sunder
    espada.crush = data.crush
    espada.pierce = data.pierce
    espada.valor_elemento = data.valor_elemento
    espada.materiales = data.materiales
    db.commit()
    db.refresh(espada)
    return espada


@app.delete("/api/espada/{id}")
def eliminar_espada(id: int, db: Session = Depends(get_db)):
    espada = db.query(Models_db.EspadaDB).filter(Models_db.EspadaDB.id == id).first()
    if not espada:
        raise HTTPException(404, "Espada no encontrada")
    db.delete(espada)
    db.commit()
    return {"mensaje": "Espada eliminada", "id": id, "nombre": espada.nombre}


# ── ESCUDO ──────────────────────────────────────────────────────────────────

@app.get("/api/escudo")
def listar_escudos(db: Session = Depends(get_db)):
    return db.query(Models_db.EscudoDB).all()


@app.get("/api/escudo/tipo/{tipo}")
def filtrar_escudo_tipo(tipo: str, db: Session = Depends(get_db)):
    return db.query(Models_db.EscudoDB).filter(
        Models_db.EscudoDB.tipo.ilike(tipo)
    ).all()


@app.get("/api/escudo/{id}")
def buscar_escudo(id: int, db: Session = Depends(get_db)):
    escudo = db.query(Models_db.EscudoDB).filter(Models_db.EscudoDB.id == id).first()
    if not escudo:
        raise HTTPException(404, "Escudo no encontrado")
    return escudo


@app.post("/api/escudo")
def crear_escudo(data: EscudoCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.EscudoDB(
        nombre=data.nombre,
        tipo=data.tipo,
        elemento=data.elemento,
        sunder=data.sunder,
        crush=data.crush,
        pierce=data.pierce,
        valor_elemento=data.valor_elemento,
        materiales=data.materiales,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.put("/api/escudo/{id}")
def actualizar_escudo(id: int, data: EscudoCreate, db: Session = Depends(get_db)):
    escudo = db.query(Models_db.EscudoDB).filter(Models_db.EscudoDB.id == id).first()
    if not escudo:
        raise HTTPException(404, "Escudo no encontrado")
    escudo.nombre = data.nombre
    escudo.tipo = data.tipo
    escudo.elemento = data.elemento
    escudo.sunder = data.sunder
    escudo.crush = data.crush
    escudo.pierce = data.pierce
    escudo.valor_elemento = data.valor_elemento
    escudo.materiales = data.materiales
    db.commit()
    db.refresh(escudo)
    return escudo


@app.delete("/api/escudo/{id}")
def eliminar_escudo(id: int, db: Session = Depends(get_db)):
    escudo = db.query(Models_db.EscudoDB).filter(Models_db.EscudoDB.id == id).first()
    if not escudo:
        raise HTTPException(404, "Escudo no encontrado")
    db.delete(escudo)
    db.commit()
    return {"mensaje": "Escudo eliminado", "id": id, "nombre": escudo.nombre}


# ── PISTOLA ──────────────────────────────────────────────────────────────────

@app.get("/api/pistola")
def listar_pistolas(db: Session = Depends(get_db)):
    return db.query(Models_db.PistolDB).all()


@app.get("/api/pistola/tipo/{tipo}")
def filtrar_pistola_tipo(tipo: str, db: Session = Depends(get_db)):
    return db.query(Models_db.PistolDB).filter(
        Models_db.PistolDB.tipo.ilike(tipo)
    ).all()


@app.get("/api/pistola/{id}")
def buscar_pistola(id: int, db: Session = Depends(get_db)):
    pistola = db.query(Models_db.PistolDB).filter(Models_db.PistolDB.id == id).first()
    if not pistola:
        raise HTTPException(404, "Pistola no encontrada")
    return pistola


@app.post("/api/pistola")
def crear_pistola(data: PistolaCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.PistolDB(
        nombre=data.nombre,
        tipo=data.tipo,
        elemento=data.elemento,
        sunder=data.sunder,
        crush=data.crush,
        pierce=data.pierce,
        valor_elemento=data.valor_elemento,
        materiales=data.materiales,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.put("/api/pistola/{id}")
def actualizar_pistola(id: int, data: PistolaCreate, db: Session = Depends(get_db)):
    pistola = db.query(Models_db.PistolDB).filter(Models_db.PistolDB.id == id).first()
    if not pistola:
        raise HTTPException(404, "Pistola no encontrada")
    pistola.nombre = data.nombre
    pistola.tipo = data.tipo
    pistola.elemento = data.elemento
    pistola.sunder = data.sunder
    pistola.crush = data.crush
    pistola.pierce = data.pierce
    pistola.valor_elemento = data.valor_elemento
    pistola.materiales = data.materiales
    db.commit()
    db.refresh(pistola)
    return pistola


@app.delete("/api/pistola/{id}")
def eliminar_pistola(id: int, db: Session = Depends(get_db)):
    pistola = db.query(Models_db.PistolDB).filter(Models_db.PistolDB.id == id).first()
    if not pistola:
        raise HTTPException(404, "Pistola no encontrada")
    db.delete(pistola)
    db.commit()
    return {"mensaje": "Pistola eliminada", "id": id, "nombre": pistola.nombre}


# ── UNIDAD DE CONTROL ────────────────────────────────────────────────────────

@app.get("/api/unidad")
def listar_unidades(db: Session = Depends(get_db)):
    return db.query(Models_db.UnidadControlDB).all()


@app.get("/api/unidad/{id}")
def buscar_unidad(id: int, db: Session = Depends(get_db)):
    unidad = db.query(Models_db.UnidadControlDB).filter(Models_db.UnidadControlDB.id == id).first()
    if not unidad:
        raise HTTPException(404, "Unidad de control no encontrada")
    return unidad


@app.post("/api/unidad")
def crear_unidad(data: UnidadControlCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.UnidadControlDB(
        nombre=data.nombre,
        tipo=data.tipo,
        buffs=data.buffs,
        materiales=data.materiales,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.put("/api/unidad/{id}")
def actualizar_unidad(id: int, data: UnidadControlCreate, db: Session = Depends(get_db)):
    unidad = db.query(Models_db.UnidadControlDB).filter(Models_db.UnidadControlDB.id == id).first()
    if not unidad:
        raise HTTPException(404, "Unidad de control no encontrada")
    unidad.nombre = data.nombre
    unidad.tipo = data.tipo
    unidad.buffs = data.buffs
    unidad.materiales = data.materiales
    db.commit()
    db.refresh(unidad)
    return unidad


@app.delete("/api/unidad/{id}")
def eliminar_unidad(id: int, db: Session = Depends(get_db)):
    unidad = db.query(Models_db.UnidadControlDB).filter(Models_db.UnidadControlDB.id == id).first()
    if not unidad:
        raise HTTPException(404, "Unidad de control no encontrada")
    db.delete(unidad)
    db.commit()
    return {"mensaje": "Unidad eliminada", "id": id, "nombre": unidad.nombre}


# ── GOD EATER ────────────────────────────────────────────────────────────────

@app.get("/api/godeater")
def listar_godeater(db: Session = Depends(get_db)):
    return db.query(Models_db.GodEaterDB).all()


@app.get("/api/godeater/rango/{rango}")
def filtrar_rango(rango: str, db: Session = Depends(get_db)):
    return db.query(Models_db.GodEaterDB).filter(
        Models_db.GodEaterDB.rango.ilike(rango)
    ).all()


@app.get("/api/godeater/{id}")
def buscar_godeater(id: int, db: Session = Depends(get_db)):
    godeater = db.query(Models_db.GodEaterDB).filter(Models_db.GodEaterDB.id == id).first()
    if not godeater:
        raise HTTPException(404, "GodEater no encontrado")
    return godeater


@app.post("/api/godeater")
def crear_godeater(data: GodEaterCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.GodEaterDB(
        nombre=data.nombre,
        rango=data.rango,
        espada_id=data.espada_id,
        escudo_id=data.escudo_id,
        pistola_id=data.pistola_id,
        unidad_id=data.unidad_id,
        descripcion=data.descripcion,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.put("/api/godeater/{id}")
def actualizar_godeater(id: int, data: GodEaterCreate, db: Session = Depends(get_db)):
    godeater = db.query(Models_db.GodEaterDB).filter(Models_db.GodEaterDB.id == id).first()
    if not godeater:
        raise HTTPException(404, "GodEater no encontrado")
    godeater.nombre = data.nombre
    godeater.rango = data.rango
    godeater.espada_id = data.espada_id
    godeater.escudo_id = data.escudo_id
    godeater.pistola_id = data.pistola_id
    godeater.unidad_id = data.unidad_id
    godeater.descripcion = data.descripcion
    db.commit()
    db.refresh(godeater)
    return godeater


@app.delete("/api/godeater/{id}")
def eliminar_godeater(id: int, db: Session = Depends(get_db)):
    godeater = db.query(Models_db.GodEaterDB).filter(Models_db.GodEaterDB.id == id).first()
    if not godeater:
        raise HTTPException(404, "GodEater no encontrado")
    db.delete(godeater)
    db.commit()
    return {"mensaje": "GodEater eliminado", "id": id, "nombre": godeater.nombre}


# ── MATERIAL ─────────────────────────────────────────────────────────────────

@app.get("/api/material")
def listar_materiales(db: Session = Depends(get_db)):
    return db.query(Models_db.MaterialDB).all()


@app.get("/api/material/origen/{origen}")
def filtrar_origen(origen: str, db: Session = Depends(get_db)):
    return db.query(Models_db.MaterialDB).filter(
        Models_db.MaterialDB.origen.ilike(origen)
    ).all()


@app.get("/api/material/rango/{rango}")
def filtrar_rango_material(rango: str, db: Session = Depends(get_db)):
    return db.query(Models_db.MaterialDB).filter(
        Models_db.MaterialDB.rango_mision == rango
    ).all()


@app.get("/api/material/{id}")
def buscar_material(id: int, db: Session = Depends(get_db)):
    material = db.query(Models_db.MaterialDB).filter(Models_db.MaterialDB.id == id).first()
    if not material:
        raise HTTPException(404, "Material no encontrado")
    return material


@app.post("/api/material")
def crear_material(data: MaterialCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.MaterialDB(
        nombre=data.nombre,
        origen=data.origen,
        rango_mision=data.rango_mision,
        obtenido_de=data.obtenido_de,
        descripcion=data.descripcion,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.put("/api/material/{id}")
def actualizar_material(id: int, data: MaterialCreate, db: Session = Depends(get_db)):
    material = db.query(Models_db.MaterialDB).filter(Models_db.MaterialDB.id == id).first()
    if not material:
        raise HTTPException(404, "Material no encontrado")
    material.nombre = data.nombre
    material.origen = data.origen
    material.rango_mision = data.rango_mision
    material.obtenido_de = data.obtenido_de
    material.descripcion = data.descripcion
    db.commit()
    db.refresh(material)
    return material


@app.delete("/api/material/{id}")
def eliminar_material(id: int, db: Session = Depends(get_db)):
    material = db.query(Models_db.MaterialDB).filter(Models_db.MaterialDB.id == id).first()
    if not material:
        raise HTTPException(404, "Material no encontrado")
    db.delete(material)
    db.commit()
    return {"mensaje": "Material eliminado", "id": id, "nombre": material.nombre}


# ── AREA ─────────────────────────────────────────────────────────────────────

@app.get("/api/area")
def listar_areas(db: Session = Depends(get_db)):
    return db.query(Models_db.AreaDB).all()


@app.get("/api/area/{id}")
def buscar_area(id: int, db: Session = Depends(get_db)):
    area = db.query(Models_db.AreaDB).filter(Models_db.AreaDB.id == id).first()
    if not area:
        raise HTTPException(404, "Área no encontrada")
    return area


@app.post("/api/area")
def crear_area(data: AreaCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.AreaDB(
        nombre=data.nombre,
        descripcion=data.descripcion,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


@app.put("/api/area/{id}")
def actualizar_area(id: int, data: AreaCreate, db: Session = Depends(get_db)):
    area = db.query(Models_db.AreaDB).filter(Models_db.AreaDB.id == id).first()
    if not area:
        raise HTTPException(404, "Área no encontrada")
    area.nombre = data.nombre
    area.descripcion = data.descripcion
    db.commit()
    db.refresh(area)
    return area


@app.delete("/api/area/{id}")
def eliminar_area(id: int, db: Session = Depends(get_db)):
    area = db.query(Models_db.AreaDB).filter(Models_db.AreaDB.id == id).first()
    if not area:
        raise HTTPException(404, "Área no encontrada")
    db.delete(area)
    db.commit()
    return {"mensaje": "Área eliminada", "id": id, "nombre": area.nombre}


# ── IMÁGENES ─────────────────────────────────────────────────────────────────

class ImagenURL(PydanticBase):
    url: str


TABLAS_IMAGEN = {
    "aragami": Models_db.AragamiDB,
    "espada": Models_db.EspadaDB,
    "escudo": Models_db.EscudoDB,
    "pistola": Models_db.PistolDB,
    "unidad": Models_db.UnidadControlDB,
    "godeater": Models_db.GodEaterDB,
    "material": Models_db.MaterialDB,
    "area": Models_db.AreaDB,
}


@app.put("/api/imagen/{tipo}/{id}")
def actualizar_imagen(tipo: str, id: int, data: ImagenURL, db: Session = Depends(get_db)):
    if tipo not in TABLAS_IMAGEN:
        raise HTTPException(400, f"Tipo inválido. Usa: {list(TABLAS_IMAGEN.keys())}")
    tabla = TABLAS_IMAGEN[tipo]
    registro = db.query(tabla).filter(tabla.id == id).first()
    if not registro:
        raise HTTPException(404, f"{tipo} con id {id} no encontrado")
    registro.imagen = data.url
    db.commit()
    db.refresh(registro)
    return {"mensaje": "Imagen actualizada", "url": registro.imagen}


@app.put("/api/imagen/area/{id}/mapa")
def actualizar_imagen_mapa(id: int, data: ImagenURL, db: Session = Depends(get_db)):
    area = db.query(Models_db.AreaDB).filter(Models_db.AreaDB.id == id).first()
    if not area:
        raise HTTPException(404, "Área no encontrada")
    area.imagen_mapa = data.url
    db.commit()
    db.refresh(area)
    return {"mensaje": "Imagen de mapa actualizada", "url": area.imagen_mapa}


@app.delete("/api/imagen/{tipo}/{id}")
def eliminar_imagen(tipo: str, id: int, db: Session = Depends(get_db)):
    if tipo not in TABLAS_IMAGEN:
        raise HTTPException(400, f"Tipo inválido. Usa: {list(TABLAS_IMAGEN.keys())}")
    tabla = TABLAS_IMAGEN[tipo]
    registro = db.query(tabla).filter(tabla.id == id).first()
    if not registro:
        raise HTTPException(404, f"{tipo} con id {id} no encontrado")
    if not registro.imagen:
        raise HTTPException(404, "Este registro no tiene imagen")
    registro.imagen = None
    db.commit()
    return {"mensaje": "Imagen eliminada"}


@app.delete("/api/imagen/area/{id}/mapa")
def eliminar_imagen_mapa(id: int, db: Session = Depends(get_db)):
    area = db.query(Models_db.AreaDB).filter(Models_db.AreaDB.id == id).first()
    if not area:
        raise HTTPException(404, "Área no encontrada")
    if not area.imagen_mapa:
        raise HTTPException(404, "Esta área no tiene imagen de mapa")
    area.imagen_mapa = None
    db.commit()
    return {"mensaje": "Imagen de mapa eliminada"}