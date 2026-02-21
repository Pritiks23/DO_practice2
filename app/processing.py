"""
Simulated background processing logic.
Replace this with real ML / transformation pipeline.
"""

import time
from .crud import update_status

def process_data(record_id: int, db):
    try:
        time.sleep(2)  # simulate processing
        update_status(db, record_id, "processed")
    except Exception:
        update_status(db, record_id, "failed")
