"""
Pydantic schemas for validation and response serialization.
"""

from pydantic import BaseModel

class IngestRequest(BaseModel):
    payload: str

class IngestResponse(BaseModel):
    id: int
    status: str

    class Config:
        orm_mode = True
