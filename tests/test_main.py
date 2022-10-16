"""Test cases for the __main__ module."""
from unittest.mock import Mock

import pytest
from click.testing import CliRunner
from pytest_mock import MockFixture

from test_hmp import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


@pytest.fixture
def mock_requests_get(mocker: MockFixture) -> Mock:
    """Fixture for mocking requests.get."""
    mock = mocker.patch("requests.get")
    mock.return_value.__enter__.return_value.json.return_value = {
        "title": "Lorem Ipsum",
        "extract": "Lorem ipsum dolor sit amet",
    }
    return mock


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
