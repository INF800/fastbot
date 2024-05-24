# Source: Whatsapp -> API setup
import os
from pprint import pprint
import httpx

from dotenv import load_dotenv

assert load_dotenv()

# Can use either of these tokens
ACCESS_TOKEN = os.environ["WA_ACCESS_TOKEN"]
LONG_LIVED_ACCESS_TOKEN = os.environ["WA_LONG_LIVED_ACCESS_TOKEN"]

PHONE_NUMBER_ID = os.environ["WA_PHONE_NUMBER_ID"]
RECIPIENT_WAID = os.environ["WA_RECIPIENT_WAID"]
GRAPH_API_VERSION = os.environ["WA_VERSION"]


url = f"https://graph.facebook.com/{GRAPH_API_VERSION}/{PHONE_NUMBER_ID}/messages"
headers = {
    # "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Authorization": f"Bearer {LONG_LIVED_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
data = {
    "messaging_product": "whatsapp",
    "to": RECIPIENT_WAID,
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {
            "code": "en_US"
        }
    }
}

response = httpx.post(url, headers=headers, json=data)

pprint(response.json())

# {'contacts': [{'input': '91x90xxxx11x', 'wa_id': '91x90xxxx11x'}],
#  'messages': [{'id': 'wamid.xxxxxxOTAxxxxxxxxExMzQwQkY5NzQ1xxxx==',
#                'message_status': 'accepted'}],
#  'messaging_product': 'whatsapp'}