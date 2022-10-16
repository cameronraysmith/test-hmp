"""Test cases for the __main__ module."""
from unittest.mock import Mock

import pytest
import requests
from click.testing import CliRunner
from pytest_mock import MockFixture

from test_hmp import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


@pytest.fixture
def mock_wikipedia_random_page(mocker: MockFixture) -> Mock:
    """Fixture for mocking wikipedia.random_page."""
    return mocker.patch("test_hmp.wikipedia.random_page")


def test_main_succeeds(runner: CliRunner, mock_requests_get: Mock) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0


def test_main_invokes_requests_get(runner, mock_requests_get: Mock) -> None:
    """It invokes requests.get."""
    runner.invoke(__main__.main)
    assert mock_requests_get.called


def test_main_prints_title(runner, mock_requests_get: Mock) -> None:
    """It prints the title of the Wikipedia page."""
    result = runner.invoke(__main__.main)
    assert "Lorem Ipsum" in result.output


def test_main_uses_en_wikipedia_org(runner, mock_requests_get):
    """It uses the English Wikipedia by default."""
    runner.invoke(__main__.main)
    args, _ = mock_requests_get.call_args
    assert "en.wikipedia.org" in args[0]


def test_main_fails_on_request_error(runner, mock_requests_get):
    """It exits with a non-zero status code if the request fails."""
    mock_requests_get.side_effect = Exception("Boom")
    result = runner.invoke(__main__.main)
    assert result.exit_code == 1


def test_main_prints_message_on_request_error(
    runner: CliRunner, mock_requests_get: Mock
) -> None:
    """It prints an error message if the request fails."""
    mock_requests_get.side_effect = requests.RequestException
    result = runner.invoke(__main__.main)
    assert "Error" in result.output
