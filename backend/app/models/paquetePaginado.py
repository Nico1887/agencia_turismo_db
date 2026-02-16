from pydantic import BaseModel
from app.models.paquete import Paquete

class PaquetePaginado(BaseModel):
    page: int
    size: int
    total: int
    total_pages: int
    data: list[Paquete]