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

