from sqlalchemy.orm import Session
from .. import models, schemas

def create(db: Session, data: schemas.ProductCreate) -> models.Product:
    obj = models.Product(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get(db: Session, product_id: int) -> models.Product | None:
    return db.get(models.Product, product_id)

def get_by_sku(db: Session, sku: str) -> models.Product | None:
    return db.query(models.Product).filter(models.Product.sku == sku).first()

def list_all(db: Session, q: str | None = None, limit: int = 50, offset: int = 0):
    query = db.query(models.Product)
    if q:
        query = query.filter(models.Product.name.ilike(f"%{q}%"))
    return query.order_by(models.Product.id.desc()).offset(offset).limit(limit).all()

def update(db: Session, product: models.Product, data: schemas.ProductUpdate) -> models.Product:
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(product, k, v)
    db.commit(); db.refresh(product)
    return product

def delete(db: Session, product: models.Product) -> None:
    db.delete(product); db.commit()
