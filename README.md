# SiGMini – Backend (T02.03)

Backend del sistema **Gestión de Minimercado (SiGMini)** implementado según la **SRS (T02.01)** y la **DDS (T02.02)**.
Incluye arquitectura modelo–repositorio–controlador–servicio y documentación **Swagger/OpenAPI**.

## Requisitos del curso (resumen)
- Repositorio con requerimientos, diseño y **tareas definidas**.
- **≥ 20 commits** mostrando trabajo progresivo.
- Servicios **funcionales** y documentados con Swagger.

## Ejecutar (FastAPI ejemplo)
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

- Swagger: http://127.0.0.1:8000/docs
- OpenAPI JSON: http://127.0.0.1:8000/openapi.json

## Estructura
- `app/models` – entidades
- `app/repositories` – persistencia
- `app/services` – reglas de negocio
- `app/api` – endpoints REST
- `tests` – pruebas unitarias/integ.

## Licencia
MIT
