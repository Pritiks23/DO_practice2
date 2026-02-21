"""
Health check endpoint for readiness & liveness probes.
"""

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "ok"}
