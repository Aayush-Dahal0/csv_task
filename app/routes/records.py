from fastapi import APIRouter
from app.services.store import get_all_records
from app.utils.responses import standard_response

router = APIRouter()

@router.get("/records")
async def get_records():
    records = get_all_records()
    return standard_response(
        success=True,
        message="Records retrieved successfully",
        data=records
    )
