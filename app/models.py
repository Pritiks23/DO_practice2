"""
Database models representing stored ingestion records.
"""

from sqlalchemy import Column, Integer, String, Text
from .database import Base

class IngestedData(Base):
    __tablename__ = "ingested_data"

    id = Column(Integer, primary_key=True, index=True)
    payload = Column(Text, nullable=False)
    status = Column(String, default="pending")  # pending | processed | failed
