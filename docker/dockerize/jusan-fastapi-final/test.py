from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_sum():
    response = client.get("/sum1n/10")
    assert response.status_code == 200
    assert response.json() == {"result": 55}

def test_fibonacci():
    response = client.get("/fibo?n=5")
    assert response.status_code == 200
    assert response.json() == {"result": 3}

def test_reverse():
    response = client.post("/reverse",headers={"string": "hello"})
    assert response.status_code == 200
    assert response.json() == {"result": "olleh"}

def test_listPut():
    response = client.put("/list", json={"element":"Apple"})
    response = client.put("/list", json={"element":"Microsoft"})
    response = client.put("/list", json={"element":"Linux"})
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple", "Microsoft", "Linux"]}

def test_listGet():
    response = client.get("/list")
    assert response.status_code == 200
    assert response.json() == {"result": ["Apple", "Microsoft", "Linux"]}
