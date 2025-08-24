from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.api import health, products

app = FastAPI(
    title="SiGMini API",
    version="1.0.0",
    description="Backend del sistema Gestión de Minimercado (T02.03). Swagger habilitado."
)

# Crear tablas
Base.metadata.create_all(bind=engine)

# Rutas
app.include_router(health.router)
app.include_router(products.router)
