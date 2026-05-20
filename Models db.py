from sqlalchemy import Column, Integer, String, JSON
from Batabase import Base


class AragamiDB(Base):
    __tablename__ = "aragami"

    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(100), nullable=False)
    tipo        = Column(String(100), nullable=False)
    debilidades = Column(JSON, default=list)
    descripcion = Column(String, nullable=True)


class GodArcDB(Base):
    __tablename__ = "godarc"

    id             = Column(Integer, primary_key=True, index=True)
    nombre         = Column(String(100), nullable=False)
    espada         = Column(JSON, nullable=False)
    escudo         = Column(JSON, nullable=False)
    pistola        = Column(JSON, nullable=False)
    unidad_control = Column(JSON, nullable=False)
    descripcion    = Column(String, nullable=True)


class GodEaterDB(Base):
    __tablename__ = "godeater"

    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(100), nullable=False)
    rango       = Column(String(100), nullable=False)
    god_arc_id  = Column(Integer, nullable=True)
    descripcion = Column(String, nullable=True)


class MaterialDB(Base):
    __tablename__ = "material"

    id            = Column(Integer, primary_key=True, index=True)
    nombre        = Column(String(100), nullable=False)
    origen        = Column(String(50), nullable=False)
    rango_mision  = Column(Integer, nullable=False)
    obtenido_de   = Column(String(100), nullable=False)
    descripcion   = Column(String, nullable=True)


class AreaDB(Base):
    __tablename__ = "area"

    id          = Column(Integer, primary_key=True, index=True)
    nombre      = Column(String(100), nullable=False)
    descripcion = Column(String, nullable=True)