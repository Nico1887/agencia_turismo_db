from pydantic import BaseModel
from typing import Optional

#Esquema de entrada
class PaqueteCreate(BaseModel):
    id : Optional[int] = None
    nombre : str
    precio : float
    nivelServicio : int
    cupo : int

#Esquema de salida(respuesta)
class PaqueteCreated(BaseModel):
    id : int
    nombre : str
    precio : float
    nivelServicio : int
    cupo : int
