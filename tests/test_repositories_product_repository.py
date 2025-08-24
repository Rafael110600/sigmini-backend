from sqlalchemy.orm import Session
from src.app.schemas import ProductCreate, ProductUpdate
from src.app.repositories import product_repository as repo
from tests.conftest import TestingSessionLocal

def test_repo_create_and_get():
    db: Session = TestingSessionLocal()
    try:
        p = repo.create(db, ProductCreate(sku="A1", name="Aceite", category="abarrotes", price=10.0, stock=5))
        got = repo.get(db, p.id)
        assert got.id == p.id and got.sku == "A1"
    finally:
        db.close()

def test_repo_update_and_delete():
    db: Session = TestingSessionLocal()
    try:
        p = repo.create(db, ProductCreate(sku="B1", name="Pan", category="panaderia", price=1.0, stock=20))
        updated = repo.update(db, p, ProductUpdate(price=1.2, stock=25))
        assert float(updated.price) == 1.2 and updated.stock == 25
        repo.delete(db, updated)
        assert repo.get(db, updated.id) is None
    finally:
        db.close()
