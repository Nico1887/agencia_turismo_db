from fastapi import FastAPI 
from app.routers.paquetes import router as paquetes
from app.core.exceptions import http_exception_handler, general_exception_handler
from fastapi import HTTPException
app = FastAPI()

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)


app.include_router(paquetes)

@app.get("/")
def read_root():
    return "Hello World!"

