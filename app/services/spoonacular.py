import requests
import os
from typing import Optional
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("SPOONACULAR_API_KEY")


def request_spoonacular(endpoint: str, params: Optional[dict] = None):
    if params is None:
        params = {}
    base_url = "https://api.spoonacular.com"
    full_url = f"{base_url}{endpoint}"
    params["apiKey"] = API_KEY
    return requests.get(full_url, params=params)
