"""Test cases for the wikipedia module."""
from unittest.mock import Mock

from test_hmp import wikipedia


def test_random_page_uses_given_language(mock_requests_get: Mock) -> None:
    """It selects the specified Wikipedia language edition."""
    wikipedia.random_page(language="de")
    args, _ = mock_requests_get.call_args
    assert "de.wikipedia.org" in args[0]
