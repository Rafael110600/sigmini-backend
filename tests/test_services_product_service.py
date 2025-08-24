import pytest
from sqlalchemy.orm import Session
from src.app.schemas import ProductCreate, ProductUpdate
from src.app.services import product_service
from tests.conftest import TestingSessionLocal

def test_service_prevents_duplicate_sku():
    db: Session = TestingSessionLocal()
    try:
        product_service.create_product(db, ProductCreate(sku="SKU-1", name="Harina"))
        with pytest.raises(ValueError):
            product_service.create_product(db, ProductCreate(sku="SKU-1", name="Harina 2"))
    finally:
        db.close()

def test_service_update_nonexistent_returns_none():
    db: Session = TestingSessionLocal()
    try:
        result = product_service.update_product(db, 9999, ProductUpdate(name="Nuevo"))
        assert result is None
    finally:
        db.close()
