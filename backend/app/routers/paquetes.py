from fastapi import APIRouter
from app.models.paquete import Paquete
from app.services.paquetes_services import listar_paquetes

router = APIRouter()


@router.get('/paquetes', response_model=list[Paquete])
def get_paquetes():
    return listar_paquetes()