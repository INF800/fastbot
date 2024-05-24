from dataclasses import dataclass
from dotenv import load_dotenv
import os

from loguru import logger


loaded = load_dotenv()

if loaded:
    logger.info("Loaded environment variables and secrets")
else:
    logger.warning("Could not environment variables and secrets")


@dataclass
class Config:
    wa_access_token: str
    wa_recipient_waid: str
    wa_phone_number_id: str
    wa_app_id: str
    wa_app_secret: str
    wa_version: str
    wa_verify_token: str
    wa_long_lived_access_token: str


def get_config() -> Config:
    return Config(
        wa_access_token=os.getenv("WA_ACCESS_TOKEN"),
        wa_recipient_waid=os.getenv("WA_RECIPIENT_WAID"),
        wa_phone_number_id=os.getenv("WA_PHONE_NUMBER_ID"),
        wa_app_id=os.getenv("WA_APP_ID"),
        wa_app_secret=os.getenv("WA_APP_SECRET"),
        wa_version=os.getenv("WA_VERSION"),
        wa_verify_token=os.getenv("WA_VERIFY_TOKEN"),
        wa_long_lived_access_token=os.getenv("WA_LONG_LIVED_ACCESS_TOKEN")
    )