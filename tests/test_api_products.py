def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_products_crud_flow(client):
    r = client.post("/products/", json={"sku": "X1", "name": "Leche", "category": "lacteos", "price": 3.5, "stock": 8})
    assert r.status_code == 201
    prod = r.json()
    pid = prod["id"]

    r = client.get("/products/?q=lec")
    assert r.status_code == 200 and len(r.json()) >= 1

    r = client.get(f"/products/{pid}")
    assert r.status_code == 200 and r.json()["sku"] == "X1"

    r = client.patch(f"/products/{pid}", json={"stock": 12})
    assert r.status_code == 200 and r.json()["stock"] == 12

    r = client.delete(f"/products/{pid}")
    assert r.status_code == 204

    r = client.get(f"/products/{pid}")
    assert r.status_code == 404

def test_api_rejects_duplicate_sku(client):
    r1 = client.post("/products/", json={"sku": "DUP", "name": "Gaseosa"})
    assert r1.status_code == 201
    r2 = client.post("/products/", json={"sku": "DUP", "name": "Otra"})
    assert r2.status_code == 400
    assert "SKU ya existe" in r2.json()["detail"]
