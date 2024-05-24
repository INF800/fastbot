from fastapi import APIRouter, FastAPI

router = APIRouter(prefix="/whatsapp",  tags=["whatsapp"])


@router.get("/status/")
async def show_status():
    return {"status": "online"}