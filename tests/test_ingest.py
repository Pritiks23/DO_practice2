def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200

def test_ingest_flow(client):
    response = client.post("/ingest", json={"payload": "test"})
    assert response.status_code == 200
    assert "id" in response.json()
