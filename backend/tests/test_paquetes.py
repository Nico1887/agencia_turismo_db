from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_paquetes_ok():
    response = client.get("/paquetes")
    assert response.status_code == 200
    assert "data" in response.json()
    assert "total" in response.json()

def test_page_invalida():
    response = client.get("/paquetes?page=0")
    assert response.status_code == 422
def test_size_invalido():
    response = client.get("/paquetes?size=200")
    assert response.status_code == 422

def test_paginacion_limite():
    response = client.get("/paquetes?page=1&size=3")
    assert response.status_code == 200
    assert len(response.json()["data"]) <= 3