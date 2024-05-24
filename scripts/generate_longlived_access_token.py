# source: https://developers.facebook.com/docs/facebook-login/guides/access-tokens/get-long-lived
import os
from pprint import pprint

import httpx
from dotenv import load_dotenv

assert load_dotenv()


APP_ID = os.environ["WA_APP_ID"]
APP_SECRET = os.environ["WA_APP_SECRET"]
ACCESS_TOKEN = os.environ["WA_ACCESS_TOKEN"]
GRAPH_API_VERSION = "v20.0"

url = "https://graph.facebook.com/{graph_api_version}/oauth/access_token"
params = {
    "grant_type": "fb_exchange_token",
    "client_id": APP_ID,
    "client_secret": APP_SECRET,
    "fb_exchange_token": ACCESS_TOKEN,
}

response = httpx.get(
    url.format(graph_api_version=GRAPH_API_VERSION), 
    params=params
)

# Contains 60 days access token
pprint(response.json())

# {'access_token': 'xxxxxXVAxdrYI9eZBktzy2ZBnUHjiLBTexxxxxxiAV9OwzqemMURqSSxxxxxxqHq3OyrQ48eF3xIZBq6Vxxxxxx',
#  'expires_in': 5182954,
#  'token_type': 'bearer'}