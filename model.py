from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class ElementoEnum(str, Enum):
    fuego  = "Fuego"
    hielo  = "Hielo"
    rayo   = "Rayo"
    divino = "Divino"

class TipoPistolaEnum(str, Enum):
    asalto        = "Asalto"
    francotirador = "Francotirador"
    escopeta      = "Escopeta"

class TipoEspadaEnum(str, Enum):
    corta = "Corta"
    larga = "Larga"
    pesada = "Pesada"


class TipoEscudoEnum(str, Enum):
    pequeno = "Buckler Shield"
    Mediano = "Shield"
    Grande = "Tower Shield"

class TipoUnidadEnum(str, Enum):
    estandar = "Estándar"
    avanzada = "Avanzada"
    suprema  = "Suprema"

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


class ParteArma(BaseModel):
    """Atributos comunes a todas las partes del GodArc."""
    sunder: int = Field(0, ge=0, description="Puntos de corte")
    crush: int = Field(0, ge=0, description="Puntos de aplastamiento")
    pierce: int = Field(0, ge=0, description="Puntos de perforación")
    elemento: ElementoEnum
    valor_elemento: int = Field(0, ge=0, description="Puntos del elemento principal")


class Espada(ParteArma):
    tipo: TipoEspadaEnum


class Escudo(ParteArma):
    tipo: TipoEscudoEnum


class Pistola(ParteArma):
    tipo: TipoPistolaEnum


class UnidadControl(BaseModel):
    tipo: TipoUnidadEnum


class GodArc(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=100)
    espada: Espada
    escudo: Escudo
    pistola: Pistola
    unidad_control: UnidadControl
    descripcion: Optional[str] = None


class GodArcCreate(BaseModel):
    nombre: str = Field(..., min_length=1, max_length=100)
    espada: Espada
    escudo: Escudo
    pistola: Pistola
    unidad_control: UnidadControl
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
