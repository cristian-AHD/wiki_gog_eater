from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class ElementoEnum(str, Enum):
    fuego = "Fuego/(Blaze)"
    rayo = "Electro/(Spark)"
    hielo = "Hielo/(Freeze)"
    divino = "Divino/(Divine)"
    veneno = "Veneno/(Poison)"

class TipoEspadaEnum(str, Enum):
    corta = "Corta"
    Larga = "Larga"
    Pesada = "Pesada"

class TipoCanonEnum(str, Enum):
    asalto = "Asalto"
    francotirador = "Francotirador"
    escopeta = "Escopeta"

class Aragami(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: str
    elemento: ElementoEnum
    debilidades: list[str] = Field(default_factory=list)
    descripcion: Optional[str] = None

class AragamiCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo: str
    elemento: ElementoEnum
    debilidades: list[str] = Field(default_factory=list)
    descripcion: Optional[str] = None


class GodArc(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo_hoja: TipoEspadaEnum
    tipo_disparo: TipoCanonEnum
    elemento: ElementoEnum
    descripcion: Optional[str] = None

class GodArcCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    tipo_hoja: TipoEspadaEnum
    tipo_disparo: TipoCanonEnum
    elemento: ElementoEnum
    descripcion: Optional[str] = None


class GodEater(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    rango: str
    god_arc_id: Optional[int] = None
    descripcion: Optional[str] = None

class GodEaterCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    rango: str
    god_arc_id: Optional[int] = None
    descripcion: Optional[str] = None