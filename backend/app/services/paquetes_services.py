import math
from fastapi import HTTPException
from app.repositories.paquetes_repo import existe_nivel_servicio, obtener_paquetes, create_paquete, obtener_paquete_via_ID, elimacion_fisica_paquete, actualizacion_paquete

def listar_paquetes(
        page: int,
        size: int,
        precio_min : float | None = None, 
        nivelServicio : int | None = None
    ):
    
    if not (size >= 1 and size <= 100):
        raise HTTPException(status_code=400, detail="El tamaño de página debe estar entre 1 y 100")

    offset = (page - 1) * size

    if precio_min is not None and precio_min < 0:
        raise HTTPException(status_code=400, detail="El precio debe ser mayor a 0")
    
    if nivelServicio is not None and (nivelServicio < 1 or nivelServicio > 3):
        raise HTTPException(status_code=400, detail="El nivel de paquete no se encuentra entre 1 y 3")
    
    paquetes, total = obtener_paquetes(precio_min, nivelServicio, offset, size)

    total_pages = math.ceil(total/size) if total > 0 else 0

    return {
        "page" : page,
        "size" : size,
        "total" : total,
        "total_pages" : total_pages,
        "data" : paquetes
    }

def crear_paquete(paquete):
    if paquete.precio <= 0:
        raise HTTPException(status_code=400, detail="El precio debe ser mayor a 0")
    if paquete.cupo <= 0:
        raise HTTPException(status_code=400, detail="El cupo debe ser mayor a 0")
    if not existe_nivel_servicio(paquete.nivelServicio):
        raise HTTPException(status_code=400, detail="Nivel de servicio invalido")
    return create_paquete(paquete)

def conseguir_paquete(id):
    paquete = obtener_paquete_via_ID(id)
    if paquete is None:
        raise HTTPException(status_code= 404, detail="No se encontro tal id")
    return paquete
    
def eliminar_paquete(id : int):
    paquete = elimacion_fisica_paquete(id)
    if paquete == False:
        raise HTTPException(status_code=404, detail="No se encontro el paquete a eliminar")
    
    return {'mensaje' : "Paquete eliminado con éxito."}

def actualizar_paquete(id, paquete):
    if paquete.precio <= 0:
        raise HTTPException(status_code=400, detail="El precio debe ser mayor a 0")
    if not paquete.nivelServicio >= 1 and paquete.nivelServicio <= 3:
        raise HTTPException(status_code=400, detail="El nivel de paquete no se encuentra entre 1 y 3")
    if paquete.cupo <=0:
        raise HTTPException(status_code=400, detail="El cupo debe ser mayor a 0")
    
    resultado = actualizacion_paquete(id, paquete)

    if resultado is None:
        raise HTTPException(status_code=404)
    return resultado