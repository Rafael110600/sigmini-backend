from sqlalchemy.orm import Session
from .. import schemas
from ..repositories import product_repository as repo

def create_product(db: Session, payload: schemas.ProductCreate):
    if repo.get_by_sku(db, payload.sku):
        raise ValueError("SKU ya existe")
    return repo.create(db, payload)

def update_product(db: Session, product_id: int, payload: schemas.ProductUpdate):
    prod = repo.get(db, product_id)
    if not prod:
        return None
    return repo.update(db, prod, payload)

def list_products(db: Session, q: str | None, limit: int, offset: int):
    return repo.list_all(db, q=q, limit=limit, offset=offset)

def get_product(db: Session, product_id: int):
    return repo.get(db, product_id)

def delete_product(db: Session, product_id: int):
    prod = repo.get(db, product_id)
    if not prod:
        return None
    repo.delete(db, prod)
    return True
