"""
Ingestion endpoints.
Handles validation, DB persistence, and background processing.
"""

from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import IngestRequest, IngestResponse
from ..crud import create_record, get_record
from ..processing import process_data

router = APIRouter()

@router.post("/ingest", response_model=IngestResponse)
def ingest_data(request: IngestRequest, background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    """
    Accepts ingestion payload.
    Persists to DB.
    Triggers async background processing.
    """
    record = create_record(db, request.payload)
    background_tasks.add_task(process_data, record.id, db)
    return record

@router.get("/ingest/{record_id}", response_model=IngestResponse)
def get_status(record_id: int, db: Session = Depends(get_db)):
    record = get_record(db, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record
