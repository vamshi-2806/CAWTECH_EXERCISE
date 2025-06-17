from fastapi import APIRouter, Body
from datetime import datetime

router = APIRouter()
feedback_store = []

@router.post("/")
def collect_feedback(feedback: dict = Body(...)):
    feedback['timestamp'] = datetime.now().isoformat()
    feedback_store.append(feedback)
    return {"status": "received", "feedback_count": len(feedback_store)}
