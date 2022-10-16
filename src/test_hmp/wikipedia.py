"""Client for the Wikipedia REST API, version 1.

See `API documentation <https://en.wikipedia.org/api/rest_v1/#/>`_.
"""
import requests


API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"


def random_page():
    """Return a random page."""
    with requests.get(API_URL) as response:
        response.raise_for_status()
        data = response.json()
    return data