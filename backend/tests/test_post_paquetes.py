from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_paquete_ok():
    nuevo_paquete = {
        "nombre": "Paquete Test",
        "precio": 1500,
        "nivelServicio": 2,
        "cupo": 20
    }

    response = client.post("/paquetes", json=nuevo_paquete)

    assert response.status_code == 201
    data = response.json()

    assert data["nombre"] == "Paquete Test"
    assert data["precio"] == 1500
    assert data["nivelServicio"] == 2
    assert data["cupo"] == 20
    assert "id" in data

def test_crear_paquete_faltan_datos():
    paquete_invalido = {
        "nombre": "Paquete Invalido"
    }

    response = client.post("/paquetes", json=paquete_invalido)

    assert response.status_code == 422

def test_crear_paquete_nivel_invalido():
    paquete_invalido = {
        "nombre": "Paquete Invalido",
        "precio": 1500,
        "nivelServicio": 10,
        "cupo": 20
    }

    response = client.post("/paquetes", json=paquete_invalido)

    assert response.status_code == 400
    assert response.json()["success"] is False