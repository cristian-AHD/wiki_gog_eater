from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from Batabase import get_db, engine
import Models_db
from Crud import CRUDCSV, Historial
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

@app.get("/aragami")
def listar_aragami(db: Session = Depends(get_db)):
    return db.query(Models_db.AragamiDB).all()


@app.get("/aragami/nombre/{nombre}")
def buscar_aragami_nombre(nombre: str, db: Session = Depends(get_db)):
    return db.query(Models_db.AragamiDB).filter(
        Models_db.AragamiDB.nombre.ilike(f"%{nombre}%")
    ).all()


@app.get("/aragami/{id}")
def buscar_aragami(id: int, db: Session = Depends(get_db)):
    aragami = db.query(Models_db.AragamiDB).filter(Models_db.AragamiDB.id == id).first()
    if not aragami:
        raise HTTPException(404, "Aragami no encontrado")
    return aragami


@app.post("/aragami")
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


@app.put("/aragami/{id}")
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


@app.delete("/aragami/{id}")
def eliminar_aragami(id: int, db: Session = Depends(get_db)):
    aragami = db.query(Models_db.AragamiDB).filter(Models_db.AragamiDB.id == id).first()
    if not aragami:
        raise HTTPException(404, "Aragami no encontrado")
    db.delete(aragami)
    db.commit()
    return {"mensaje": "Aragami eliminado", "id": id, "nombre": aragami.nombre}


# ── Espada ────────────────────────────────────────────────────────────────────

@app.get("/espada")
def listar_espadas(db: Session = Depends(get_db)):
    return db.query(Models_db.EspadaDB).all()


@app.get("/espada/tipo/{tipo}")
def filtrar_espada_tipo(tipo: str, db: Session = Depends(get_db)):
    return db.query(Models_db.EspadaDB).filter(
        Models_db.EspadaDB.tipo.ilike(tipo)
    ).all()


@app.get("/espada/{id}")
def buscar_espada(id: int, db: Session = Depends(get_db)):
    espada = db.query(Models_db.EspadaDB).filter(Models_db.EspadaDB.id == id).first()
    if not espada:
        raise HTTPException(404, "Espada no encontrada")
    return espada


@app.post("/espada")
def crear_espada(data: EspadaCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.EspadaDB(
        nombre=data.nombre, tipo=data.tipo.value,
        elemento=data.elemento.value, sunder=data.sunder,
        crush=data.crush, pierce=data.pierce,
        valor_elemento=data.valor_elemento,
        materiales=data.materiales, descripcion=data.descripcion,
    )
    db.add(nuevo);
    db.commit();
    db.refresh(nuevo)
    return nuevo


@app.put("/espada/{id}")
def actualizar_espada(id: int, data: EspadaCreate, db: Session = Depends(get_db)):
    espada = db.query(Models_db.EspadaDB).filter(Models_db.EspadaDB.id == id).first()
    if not espada:
        raise HTTPException(404, "Espada no encontrada")
    espada.nombre = data.nombre;
    espada.tipo = data.tipo.value
    espada.elemento = data.elemento.value;
    espada.sunder = data.sunder
    espada.crush = data.crush;
    espada.pierce = data.pierce
    espada.valor_elemento = data.valor_elemento
    espada.materiales = data.materiales;
    espada.descripcion = data.descripcion
    db.commit();
    db.refresh(espada)
    return espada


@app.delete("/espada/{id}")
def eliminar_espada(id: int, db: Session = Depends(get_db)):
    espada = db.query(Models_db.EspadaDB).filter(Models_db.EspadaDB.id == id).first()
    if not espada:
        raise HTTPException(404, "Espada no encontrada")
    db.delete(espada);
    db.commit()
    return {"mensaje": "Espada eliminada", "id": id, "nombre": espada.nombre}



@app.get("/escudo")
def listar_escudos(db: Session = Depends(get_db)):
    return db.query(Models_db.EscudoDB).all()


@app.get("/escudo/tipo/{tipo}")
def filtrar_escudo_tipo(tipo: str, db: Session = Depends(get_db)):
    return db.query(Models_db.EscudoDB).filter(
        Models_db.EscudoDB.tipo.ilike(tipo)
    ).all()


@app.get("/escudo/{id}")
def buscar_escudo(id: int, db: Session = Depends(get_db)):
    escudo = db.query(Models_db.EscudoDB).filter(Models_db.EscudoDB.id == id).first()
    if not escudo:
        raise HTTPException(404, "Escudo no encontrado")
    return escudo


@app.post("/escudo")
def crear_escudo(data: EscudoCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.EscudoDB(
        nombre=data.nombre, tipo=data.tipo.value,
        elemento=data.elemento.value, sunder=data.sunder,
        crush=data.crush, pierce=data.pierce,
        valor_elemento=data.valor_elemento,
        materiales=data.materiales, descripcion=data.descripcion,
    )
    db.add(nuevo);
    db.commit();
    db.refresh(nuevo)
    return nuevo


@app.put("/escudo/{id}")
def actualizar_escudo(id: int, data: EscudoCreate, db: Session = Depends(get_db)):
    escudo = db.query(Models_db.EscudoDB).filter(Models_db.EscudoDB.id == id).first()
    if not escudo:
        raise HTTPException(404, "Escudo no encontrado")
    escudo.nombre = data.nombre;
    escudo.tipo = data.tipo.value
    escudo.elemento = data.elemento.value;
    escudo.sunder = data.sunder
    escudo.crush = data.crush;
    escudo.pierce = data.pierce
    escudo.valor_elemento = data.valor_elemento
    escudo.materiales = data.materiales;
    escudo.descripcion = data.descripcion
    db.commit();
    db.refresh(escudo)
    return escudo


@app.delete("/escudo/{id}")
def eliminar_escudo(id: int, db: Session = Depends(get_db)):
    escudo = db.query(Models_db.EscudoDB).filter(Models_db.EscudoDB.id == id).first()
    if not escudo:
        raise HTTPException(404, "Escudo no encontrado")
    db.delete(escudo);
    db.commit()
    return {"mensaje": "Escudo eliminado", "id": id, "nombre": escudo.nombre}


# ── Pistola ───────────────────────────────────────────────────────────────────

@app.get("/pistola")
def listar_pistolas(db: Session = Depends(get_db)):
    return db.query(Models_db.PistolDB).all()


@app.get("/pistola/tipo/{tipo}")
def filtrar_pistola_tipo(tipo: str, db: Session = Depends(get_db)):
    return db.query(Models_db.PistolDB).filter(
        Models_db.PistolDB.tipo.ilike(tipo)
    ).all()


@app.get("/pistola/{id}")
def buscar_pistola(id: int, db: Session = Depends(get_db)):
    pistola = db.query(Models_db.PistolDB).filter(Models_db.PistolDB.id == id).first()
    if not pistola:
        raise HTTPException(404, "Pistola no encontrada")
    return pistola


@app.post("/pistola")
def crear_pistola(data: PistolaCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.PistolDB(
        nombre=data.nombre, tipo=data.tipo.value,
        elemento=data.elemento.value, sunder=data.sunder,
        crush=data.crush, pierce=data.pierce,
        valor_elemento=data.valor_elemento,
        materiales=data.materiales, descripcion=data.descripcion,
    )
    db.add(nuevo);
    db.commit();
    db.refresh(nuevo)
    return nuevo


@app.put("/pistola/{id}")
def actualizar_pistola(id: int, data: PistolaCreate, db: Session = Depends(get_db)):
    pistola = db.query(Models_db.PistolDB).filter(Models_db.PistolDB.id == id).first()
    if not pistola:
        raise HTTPException(404, "Pistola no encontrada")
    pistola.nombre = data.nombre;
    pistola.tipo = data.tipo.value
    pistola.elemento = data.elemento.value;
    pistola.sunder = data.sunder
    pistola.crush = data.crush;
    pistola.pierce = data.pierce
    pistola.valor_elemento = data.valor_elemento
    pistola.materiales = data.materiales;
    pistola.descripcion = data.descripcion
    db.commit();
    db.refresh(pistola)
    return pistola


@app.delete("/pistola/{id}")
def eliminar_pistola(id: int, db: Session = Depends(get_db)):
    pistola = db.query(Models_db.PistolDB).filter(Models_db.PistolDB.id == id).first()
    if not pistola:
        raise HTTPException(404, "Pistola no encontrada")
    db.delete(pistola);
    db.commit()
    return {"mensaje": "Pistola eliminada", "id": id, "nombre": pistola.nombre}


# ── Unidad de Control ─────────────────────────────────────────────────────────

@app.get("/unidad")
def listar_unidades(db: Session = Depends(get_db)):
    return db.query(Models_db.UnidadControlDB).all()


@app.get("/unidad/{id}")
def buscar_unidad(id: int, db: Session = Depends(get_db)):
    unidad = db.query(Models_db.UnidadControlDB).filter(Models_db.UnidadControlDB.id == id).first()
    if not unidad:
        raise HTTPException(404, "Unidad de control no encontrada")
    return unidad


@app.post("/unidad")
def crear_unidad(data: UnidadControlCreate, db: Session = Depends(get_db)):
    nuevo = Models_db.UnidadControlDB(
        nombre=data.nombre, tipo=data.tipo.value,
        buffs=data.buffs, materiales=data.materiales,
        descripcion=data.descripcion,
    )
    db.add(nuevo),
    db.commit(),
    db.refresh(nuevo)
    return nuevo


@app.put("/unidad/{id}")
def actualizar_unidad(id: int, data: UnidadControlCreate, db: Session = Depends(get_db)):
    unidad = db.query(Models_db.UnidadControlDB).filter(Models_db.UnidadControlDB.id == id).first()
    if not unidad:
        raise HTTPException(404, "Unidad de control no encontrada")
    unidad.nombre = data.nombre;
    unidad.tipo = data.tipo.value
    unidad.buffs = data.buffs;
    unidad.materiales = data.materiales
    unidad.descripcion = data.descripcion
    db.commit();
    db.refresh(unidad)
    return unidad


@app.delete("/unidad/{id}")
def eliminar_unidad(id: int, db: Session = Depends(get_db)):
    unidad = db.query(Models_db.UnidadControlDB).filter(Models_db.UnidadControlDB.id == id).first()
    if not unidad:
        raise HTTPException(404, "Unidad de control no encontrada")
    db.delete(unidad);
    db.commit()
    return {"mensaje": "Unidad eliminada", "id": id, "nombre": unidad.nombre}


# ── GodEater ──────────────────────────────────────────────────────────────────

@app.get("/godeater")
def listar_godeater(db: Session = Depends(get_db)):
    return db.query(Models_db.GodEaterDB).all()


@app.get("/godeater/rango/")
def filtrar_rango(rango: str, db: Session = Depends(get_db)):
    return db.query(Models_db.GodEaterDB).filter(
        Models_db.GodEaterDB.rango.ilike(rango)
    ).all()


@app.get("/godeater/id")
def buscar_godeater(id: int, db: Session = Depends(get_db)):
    godeater = db.query(Models_db.GodEaterDB).filter(models_db.GodEaterDB.id == id).first()
    if not godeater:
        raise HTTPException(404, "GodEater no encontrado")
    return godeater


@app.post("/godeater")
def crear_godeater(data: GodEaterCreate, db: Session = Depends(get_db)):
    # Validar que los IDs referenciados existan
    if data.espada_id and not db.query(Models_db.EspadaDB).filter(Models_db.EspadaDB.id == data.espada_id).first():
        raise HTTPException(404, "Espada no encontrada")
    if data.escudo_id and not db.query(Models_db.EscudoDB).filter(Models_db.EscudoDB.id == data.escudo_id).first():
        raise HTTPException(404, "Escudo no encontrado")
    if data.pistola_id and not db.query(Models_db.PistolDB).filter(Models_db.PistolDB.id == data.pistola_id).first():
        raise HTTPException(404, "Pistola no encontrada")
    if data.unidad_id and not db.query(Models_db.UnidadControlDB).filter(
            Models_db.UnidadControlDB.id == data.unidad_id).first():
        raise HTTPException(404, "Unidad de control no encontrada")

    nuevo = Models_db.GodEaterDB(
        nombre=data.nombre, rango=data.rango,
        espada_id=data.espada_id, escudo_id=data.escudo_id,
        pistola_id=data.pistola_id, unidad_id=data.unidad_id,
        descripcion=data.descripcion,
    )
    db.add(nuevo);
    db.commit();
    db.refresh(nuevo)
    return nuevo


@app.put("/godeater/{id}")
def actualizar_godeater(id: int, data: GodEaterCreate, db: Session = Depends(get_db)):
    godeater = db.query(Models_db.GodEaterDB).filter(Models_db.GodEaterDB.id == id).first()
    if not godeater:
        raise HTTPException(404, "GodEater no encontrado")
    if data.espada_id and not db.query(Models_db.EspadaDB).filter(Models_db.EspadaDB.id == data.espada_id).first():
        raise HTTPException(404, "Espada no encontrada")
    if data.escudo_id and not db.query(Models_db.EscudoDB).filter(Models_db.EscudoDB.id == data.escudo_id).first():
        raise HTTPException(404, "Escudo no encontrado")
    if data.pistola_id and not db.query(Models_db.PistolDB).filter(Models_db.PistolDB.id == data.pistola_id).first():
        raise HTTPException(404, "Pistola no encontrada")
    if data.unidad_id and not db.query(models_db.UnidadControlDB).filter(
            models_db.UnidadControlDB.id == data.unidad_id).first():
        raise HTTPException(404, "Unidad de control no encontrada")
    godeater.nombre = data.nombre;
    godeater.rango = data.rango
    godeater.espada_id = data.espada_id;
    godeater.escudo_id = data.escudo_id
    godeater.pistola_id = data.pistola_id;
    godeater.unidad_id = data.unidad_id
    godeater.descripcion = data.descripcion
    db.commit();
    db.refresh(godeater)
    return godeater


@app.delete("/godeater/{id}")
def eliminar_godeater(id: int, db: Session = Depends(get_db)):
    godeater = db.query(models_db.GodEaterDB).filter(models_db.GodEaterDB.id == id).first()
    if not godeater:
        raise HTTPException(404, "GodEater no encontrado")
    db.delete(godeater);
    db.commit()
    return {"mensaje": "GodEater eliminado", "id": id, "nombre": godeater.nombre}


# ── Material ──────────────────────────────────────────────────────────────────

@app.get("/material")
def listar_materiales(db: Session = Depends(get_db)):
    return db.query(models_db.MaterialDB).all()


@app.get("/material/origen/{origen}")
def filtrar_origen(origen: str, db: Session = Depends(get_db)):
    return db.query(models_db.MaterialDB).filter(
        models_db.MaterialDB.origen.ilike(origen)
    ).all()


@app.get("/material/rango/{rango}")
def filtrar_rango_material(rango: int, db: Session = Depends(get_db)):
    return db.query(models_db.MaterialDB).filter(
        models_db.MaterialDB.rango_mision == rango
    ).all()


@app.get("/material/{id}")
def buscar_material(id: int, db: Session = Depends(get_db)):
    material = db.query(models_db.MaterialDB).filter(models_db.MaterialDB.id == id).first()
    if not material:
        raise HTTPException(404, "Material no encontrado")
    return material


@app.post("/material")
def crear_material(data: MaterialCreate, db: Session = Depends(get_db)):
    nuevo = models_db.MaterialDB(
        nombre=data.nombre, origen=data.origen.value,
        rango_mision=data.rango_mision, obtenido_de=data.obtenido_de,
        descripcion=data.descripcion,
    )
    db.add(nuevo);
    db.commit();
    db.refresh(nuevo)
    return nuevo


@app.put("/material/{id}")
def actualizar_material(id: int, data: MaterialCreate, db: Session = Depends(get_db)):
    material = db.query(models_db.MaterialDB).filter(models_db.MaterialDB.id == id).first()
    if not material:
        raise HTTPException(404, "Material no encontrado")
    material.nombre = data.nombre;
    material.origen = data.origen.value
    material.rango_mision = data.rango_mision;
    material.obtenido_de = data.obtenido_de
    material.descripcion = data.descripcion
    db.commit();
    db.refresh(material)
    return material


@app.delete("/material/{id}")
def eliminar_material(id: int, db: Session = Depends(get_db)):
    material = db.query(models_db.MaterialDB).filter(models_db.MaterialDB.id == id).first()
    if not material:
        raise HTTPException(404, "Material no encontrado")
    db.delete(material);
    db.commit()
    return {"mensaje": "Material eliminado", "id": id, "nombre": material.nombre}


# ── Area ──────────────────────────────────────────────────────────────────────

@app.get("/area")
def listar_areas(db: Session = Depends(get_db)):
    return db.query(models_db.AreaDB).all()


@app.get("/area/{id}")
def buscar_area(id: int, db: Session = Depends(get_db)):
    area = db.query(models_db.AreaDB).filter(models_db.AreaDB.id == id).first()
    if not area:
        raise HTTPException(404, "Área no encontrada")
    return area


@app.post("/area")
def crear_area(data: AreaCreate, db: Session = Depends(get_db)):
    nuevo = models_db.AreaDB(nombre=data.nombre, descripcion=data.descripcion)
    db.add(nuevo);
    db.commit();
    db.refresh(nuevo)
    return nuevo


@app.put("/area/{id}")
def actualizar_area(id: int, data: AreaCreate, db: Session = Depends(get_db)):
    area = db.query(models_db.AreaDB).filter(models_db.AreaDB.id == id).first()
    if not area:
        raise HTTPException(404, "Área no encontrada")
    area.nombre = data.nombre;
    area.descripcion = data.descripcion
    db.commit();
    db.refresh(area)
    return area


@app.delete("/area/{id}")
def eliminar_area(id: int, db: Session = Depends(get_db)):
    area = db.query(Models_db.AreaDB).filter(Models_db.AreaDB.id == id).first()
    if not area:
        raise HTTPException(404, "Área no encontrada")
    db.delete(area);
    db.commit()
    return {"mensaje": "Área eliminada", "id": id, "nombre": area.nombre}