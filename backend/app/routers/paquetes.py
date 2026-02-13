from fastapi import APIRouter, HTTPException, status, Query
from app.models.paquete import Paquete
from app.models.paqueteCreate import PaqueteCreated, PaqueteCreate
from app.models.paqueteNuevo import PaqueteNuevo, PaqueteNuevoSalida
from app.services.paquetes_services import listar_paquetes, crear_paquete, conseguir_paquete, eliminar_paquete, actualizar_paquete

router = APIRouter()


@router.get('/paquetes', response_model=list[Paquete])
def get_paquetes(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100),
    precio_min: float | None = None,
    nivelServicio: int | None = None
):

    return listar_paquetes(page, size, precio_min, nivelServicio)

@router.post('/paquetes', response_model =PaqueteCreated)
def post_paquetes(paquete : PaqueteCreate):
    return crear_paquete(paquete)

@router.get('/paquetes/{id}', response_model=Paquete)
def get_paquete_via_id(id : int):
    return conseguir_paquete(id)
    
@router.delete('/paquetes/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_paquete(id : int):
    return eliminar_paquete(id)

@router.put('/paquetes/{id}', response_model=PaqueteNuevoSalida)
def put_paquete(id: int, nuevos_datos: PaqueteNuevo):
    return actualizar_paquete(id, nuevos_datos)