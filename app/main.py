"""
Application entry point.
Initializes DB and registers routers.
"""

from fastapi import FastAPI
from .database import Base, engine
from .routers import ingest, health

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Data Ingestion Service")

app.include_router(health.router)
app.include_router(ingest.router)
