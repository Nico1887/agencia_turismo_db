from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_eliminar_paquete_ok():
    response = client.delete("/paquetes/148")

    assert response.status_code == 204
    assert response.content == b""

def test_eliminar_paquete_inexistente():
    response = client.delete("/paquetes/9999")

    assert response.status_code == 404
    data = response.json()

    assert data["success"] is False
    assert data["error"]["code"] == 404