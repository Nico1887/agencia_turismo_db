from pydantic import BaseModel

class Paquete(BaseModel):
    id : int
    nombre : str
    precio : float
    nivelServicio : int
    cupo : int
    