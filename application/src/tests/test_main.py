from fastapi.testclient import TestClient
from src import main

client = TestClient(main.app)

def test_root():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {"Hello": "World"}

def test_items():
  response = client.get("/items/2?q=my-query")
  assert response.status_code == 200
  assert response.json() == {"item_id": 2, "q": "my-query"}
