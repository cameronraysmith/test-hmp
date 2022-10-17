"""Client for the Wikipedia REST API, version 1.

See `API documentation <https://en.wikipedia.org/api/rest_v1/#/>`_.
"""
from typing import Any

import click
import requests


API_URL = "https://{language}.wikipedia.org/api/rest_v1/page/random/summary"


def random_page(language: str = "en") -> Any:
    """Return a random page."""
    url = API_URL.format(language=language)

    try:
        with requests.get(url) as response:
            response.raise_for_status()
            data = response.json()
        return data
    except requests.RequestException as error:
        message = str(error)
        raise click.ClickException(message) from error
