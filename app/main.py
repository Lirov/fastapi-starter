from fastapi import FastAPI
from app.routers import auth_router, health_router

def create_app() -> FastAPI:
    app = FastAPI(title="FastAPI Starter", version="0.1.0")
    app.include_router(health_router.router)
    app.include_router(auth_router.router)
    return app

app = create_app()
