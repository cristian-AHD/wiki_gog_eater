from sqlalchemy import Column, Integer, String, JSON
from Batabase import Base


class AragamiDB(Base):
    __tablename__ = "aragami"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(100), nullable=False)
    debilidades = Column(JSON, default=list)
    descripcion = Column(String, nullable=True)
    imagen = Column(String, nullable=True)


class EspadaDB(Base):
    __tablename__ = "espada"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    elementos = Column(JSON, default=list)   # [{"elemento": "Fuego", "valor": 150}, ...]
    sunder = Column(Integer, default=0)
    crush = Column(Integer, default=0)
    pierce = Column(Integer, default=0)
    materiales = Column(JSON, default=list)
    imagen = Column(String, nullable=True)


class EscudoDB(Base):
    __tablename__ = "escudo"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    elementos = Column(JSON, default=list)   # [{"elemento": "Hielo", "valor": 100}, ...]
    sunder = Column(Integer, default=0)
    crush = Column(Integer, default=0)
    pierce = Column(Integer, default=0)
    materiales = Column(JSON, default=list)
    imagen = Column(String, nullable=True)


class PistolDB(Base):
    __tablename__ = "pistola"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    elementos = Column(JSON, default=list)   # [{"elemento": "Rayo", "valor": 200}, ...]
    sunder = Column(Integer, default=0)
    crush = Column(Integer, default=0)
    pierce = Column(Integer, default=0)
    materiales = Column(JSON, default=list)
    imagen = Column(String, nullable=True)


class UnidadControlDB(Base):
    __tablename__ = "unidad_control"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo = Column(String(50), nullable=False)
    buffs = Column(String, nullable=False)
    materiales = Column(JSON, default=list)
    imagen = Column(String, nullable=True)


class GodEaterDB(Base):
    __tablename__ = "godeater"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    rango = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=True)
    imagen = Column(String, nullable=True)


class MaterialDB(Base):
    __tablename__ = "material"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    origen = Column(String(50), nullable=False)
    rango_mision = Column(String(10), nullable=False)
    obtenido_de = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=True)
    imagen = Column(String, nullable=True)


class AreaDB(Base):
    __tablename__ = "area"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=True)
    imagen = Column(String, nullable=True)
    imagen_mapa = Column(String, nullable=True)