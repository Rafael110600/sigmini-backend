from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas
from ..services import product_service

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/", response_model=list[schemas.ProductOut])
def list_products(q: str | None = Query(None), limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    return product_service.list_products(db, q=q, limit=limit, offset=offset)

@router.post("/", response_model=schemas.ProductOut, status_code=201)
def create_product(payload: schemas.ProductCreate, db: Session = Depends(get_db)):
    try:
        return product_service.create_product(db, payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    prod = product_service.get_product(db, product_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return prod

@router.patch("/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, payload: schemas.ProductUpdate, db: Session = Depends(get_db)):
    prod = product_service.update_product(db, product_id, payload)
    if not prod:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return prod

@router.delete("/{product_id}", status_code=204)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    ok = product_service.delete_product(db, product_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return None
