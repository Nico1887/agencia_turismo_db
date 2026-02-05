from fastapi import FastAPI 
from app.routers.paquetes import router as paquetes
app = FastAPI()

app.include_router(paquetes)

@app.get("/")
def read_root():
    return "Hello World!"

