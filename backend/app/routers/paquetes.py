from fastapi import APIRouter
from app.models.paquete import Paquete
from app.models.paqueteCreate import PaqueteCreated, PaqueteCreate
from app.services.paquetes_services import listar_paquetes, crear_paquete

router = APIRouter()


@router.get('/paquetes', response_model=list[Paquete])
def get_paquetes():
    return listar_paquetes()

@router.post('/paquetes', response_model =PaqueteCreated)
def post_paquetes(paquete : PaqueteCreate):
    return crear_paquete(paquete)