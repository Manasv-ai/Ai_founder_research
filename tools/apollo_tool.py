import requests
import os

APOLLO_API_KEY = os.getenv("APOLLO_API_KEY")

def search_founders(keyword):

    url = "https://api.apollo.io/v1/mixed_people/search"

    headers = {
        "Content-Type": "application/json",
        "Cache-Control": "no-cache"
    }

    data = {
        "q_keywords": keyword,
        "page": 1
    }

    response = requests.post(url, json=data, headers=headers)

    return response.json()