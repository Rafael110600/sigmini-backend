from sqlalchemy import String, Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Product(Base):
    __tablename__ = "products"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    sku: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(200), index=True)
    category: Mapped[str] = mapped_column(String(100), default="general")
    price: Mapped[float] = mapped_column(Numeric(10, 2), default=0)
    stock: Mapped[int] = mapped_column(Integer, default=0)
