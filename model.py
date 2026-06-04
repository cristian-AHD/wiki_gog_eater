from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class ElementoEnum(str, Enum):
    fuego  = "Fuego"
    hielo  = "Hielo"
    rayo   = "Rayo"
    divino = "Divino"
    ninguno = "Ninguno"


class TipoEspadaEnum(str, Enum):
    corta = "Corta"
    larga = "Larga"
    pesada = "Pesada"


class TipoEscudoEnum(str, Enum):
    buckler = "Buckler Shield"
    mediano = "Shield"
    torre = "Tower Shield"


class TipoPistolaEnum(str, Enum):
    asalto = "Asalto"
    francotirador = "Francotirador"
    escopeta = "Escopeta"


class TipoUnidadEnum(str, Enum):
    estandar = "Estándar"
    avanzada = "Avanzada"
    suprema = "Suprema"


class OrigenEnum(str, Enum):
    aragami = "Aragami"
    objetivo_perdido = "Objetivo Perdido"


class Aragami(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: str
    debilidades: list[str] = Field(default_factory=list)
    descripcion: Optional[str] = None


class AragamiCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: str
    debilidades: list[str] = Field(default_factory=list)
    descripcion: Optional[str] = None

class Espada(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: TipoEspadaEnum
    elemento: ElementoEnum
    sunder: int = Field(0, ge=0)
    crush: int = Field(0, ge=0)
    pierce: int = Field(0, ge=0)
    valor_elemento: int = Field(0, ge=0)
    materiales: list[str] = Field(default_factory=list, description="Ej: ['3x Garra de Ogretail']")


class EspadaCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: TipoEspadaEnum
    elemento: ElementoEnum
    sunder: int = Field(0, ge=0)
    crush: int = Field(0, ge=0)
    pierce: int = Field(0, ge=0)
    valor_elemento: int = Field(0, ge=0)
    materiales: list[str] = Field(default_factory=list)


class Escudo(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: TipoEscudoEnum
    elemento: ElementoEnum
    sunder: int = Field(0, ge=0)
    crush: int = Field(0, ge=0)
    pierce: int = Field(0, ge=0)
    valor_elemento: int = Field(0, ge=0)
    materiales: list[str] = Field(default_factory=list)


class EscudoCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: TipoEscudoEnum
    elemento: ElementoEnum
    sunder: int = Field(0, ge=0)
    crush: int = Field(0, ge=0)
    pierce: int = Field(0, ge=0)
    valor_elemento: int = Field(0, ge=0)
    materiales: list[str] = Field(default_factory=list)


class Pistola(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: TipoPistolaEnum
    elemento: ElementoEnum
    sunder: int = Field(0, ge=0)
    crush: int = Field(0, ge=0)
    pierce: int = Field(0, ge=0)
    valor_elemento: int = Field(0, ge=0)
    materiales: list[str] = Field(default_factory=list)


class PistolaCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: TipoPistolaEnum
    elemento: ElementoEnum
    sunder: int = Field(0, ge=0)
    crush: int = Field(0, ge=0)
    pierce: int = Field(0, ge=0)
    valor_elemento: int = Field(0, ge=0)
    materiales: list[str] = Field(default_factory=list)


class UnidadControl(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: TipoUnidadEnum
    buffs: str = Field(..., description="Descripción de los buffs del traje")
    materiales: list[str] = Field(default_factory=list)


class UnidadControlCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: TipoUnidadEnum
    buffs: str = Field(..., description="Descripción de los buffs del traje")
    materiales: list[str] = Field(default_factory=list)


class GodEater(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    rango: str
    espada_id: Optional[int] = None
    escudo_id: Optional[int] = None
    pistola_id: Optional[int] = None
    unidad_id: Optional[int] = None
    descripcion: Optional[str] = None


class GodEaterCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    rango: str
    espada_id: Optional[int] = None
    escudo_id: Optional[int] = None
    pistola_id: Optional[int] = None
    unidad_id: Optional[int] = None
    descripcion: Optional[str] = None


class Material(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    origen: OrigenEnum
    rango_mision: int = Field(..., ge=1, le=10)
    obtenido_de: str
    descripcion: Optional[str] = None


class MaterialCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    origen: OrigenEnum
    rango_mision: int = Field(..., ge=1, le=10)
    obtenido_de: str
    descripcion: Optional[str] = None


class Area(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = None
    imagen: Optional[str] = None
    imagen_mapa: Optional[str] = None


class AreaCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    descripcion: Optional[str] = None
