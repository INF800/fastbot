from loguru import logger
from fastapi import APIRouter, Request, HTTPException, Response

from fastbot.whatsapp._webhook import router as webhook_router
from fastbot.config import get_config

config = get_config()

router = APIRouter(prefix="/whatsapp",  tags=["whatsapp"])

router.include_router(webhook_router)

@router.get("/")
def whatsapp():
    return {"status": "online"}