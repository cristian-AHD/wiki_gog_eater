from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class ElementoEnum(str, Enum):
    fuego = "Fuego"
    agua = "Agua"
    rayo = "Rayo"
    hielo = "Hielo"
    divino = "Divino"
    neutro = "Neutro"
