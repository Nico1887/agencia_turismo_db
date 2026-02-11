from pydantic import BaseModel

class PaqueteNuevo(BaseModel):
    nombre : str
    precio : float
    nivelServicio : int
    cupo : int

class PaqueteNuevoSalida(BaseModel):
    id : int 
    nombre: str
    precio : float
    nivelServicio : int
    cupo : int