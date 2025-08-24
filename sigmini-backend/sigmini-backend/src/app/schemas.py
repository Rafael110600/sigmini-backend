from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    sku: str = Field(..., min_length=1)
    name: str
    category: str | None = "general"
    price: float = 0
    stock: int = 0

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    price: float | None = None
    stock: int | None = None

class ProductOut(ProductBase):
    id: int
    class Config:
        from_attributes = True
