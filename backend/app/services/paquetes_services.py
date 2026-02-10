from fastapi import HTTPException
from app.repositories.paquetes_repo import obtener_paquetes, create_paquete

def listar_paquetes():
    return obtener_paquetes()

def crear_paquete(paquete):
    if paquete.precio <= 0:
        raise HTTPException(status_code=400, detail="El precio debe ser mayor a 0")
    if paquete.cupo <= 0:
        raise HTTPException(status_code=400, detail="El cupo debe ser mayor a 0")
    return create_paquete(paquete)

