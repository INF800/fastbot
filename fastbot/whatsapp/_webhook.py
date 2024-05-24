from datetime import datetime
import json
from functools import wraps
import hashlib
import hmac
from typing import Tuple

from loguru import logger
from fastapi import APIRouter, Request, HTTPException, Response

from fastbot.config import get_config
from fastbot.whatsapp.utils import (
    is_valid_whatsapp_message,
)


config = get_config()

router = APIRouter(prefix="/webhook",  tags=["whatsapp"])


def validate_signature(payload: bytes, signature: str) -> bool:
    expected_signature = hmac.new(
        bytes(config.wa_app_secret, "latin-1"),
        msg=payload,
        digestmod=hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(expected_signature, signature)


async def signature_required(request: Request, app_secret: str = config.wa_app_secret) -> None:
    signature = request.headers.get("X-Hub-Signature-256", "")[7:]  # Removing 'sha256='
    if not validate_signature(await request.body(), signature):
        logger.info("Signature verification failed!")
        raise HTTPException(status_code=403, detail="Invalid signature")


@router.get("/")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == config.wa_verify_token:
            logger.info("Webhook verified successfully!")
            headers = {
                "Server": "Werkzeug/3.0.3 Python/3.10.11",
                "Date": datetime.now().strftime("%a, %d %b %Y %H:%M:%S GMT"),
                "Content-Type": "text/html; charset=utf-8",
                "Content-Length": str(len(challenge)),
                "Connection": "close"
            }
            return Response(content=challenge, headers=headers)
        else:
            logger.info("Webhook verification failed")
            raise HTTPException(status_code=403, detail="Verification failed")
    else:
        logger.debug("Either mode or token or both are absent")


@router.post("/")
async def process_message(request: Request):
    await signature_required(request)
    body = await request.json()

    if (
        body.get("entry", [{}])[0]
        .get("changes", [{}])[0]
        .get("value", {})
        .get("statuses")
    ):
        logger.info("Received a WhatsApp status update.")
        return {"status": "ok"}

    try:
        if is_valid_whatsapp_message(body):
            body_string = json.dumps(body, indent=4)
            logger.info(f"Received message: \n{body_string}")
            return {"status": "ok"}
        else:
            raise HTTPException(status_code=404, detail="Not a WhatsApp API event")
    except json.JSONDecodeError:
        logger.error("Failed to decode JSON")
        raise HTTPException(status_code=400, detail="Invalid JSON provided")
