from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # 👈 importar CORS
from app.database import Base, engine
from app import models
from app.api import health, products

app = FastAPI(
    title="SiGMini API",
    version="1.0.0",
    description="Backend del sistema Gestión de Minimercado (T02.03). Swagger habilitado."
)

# 👇 Configuración CORS
origins = [
    "http://localhost:5173",   # frontend en Vite
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas
Base.metadata.create_all(bind=engine)

# Rutas
app.include_router(health.router)
app.include_router(products.router)
