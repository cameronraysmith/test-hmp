"""Command-line interface."""

import textwrap

import click

from . import __version__
from . import wikipedia


@click.command()
@click.option(
    "--language",
    "-l",
    default="en",
    help="Language edition of Wikipedia",
    metavar="LANG",
    show_default=True,
)
@click.version_option(version=__version__)
def main(language: str) -> None:
    """Test Hypermodern Python."""
    data = wikipedia.random_page(language=language)

    title = data["title"]
    extract = data["extract"]

    click.secho(title, fg="green")
    click.echo(textwrap.fill(extract))


if __name__ == "__main__":
    main(prog_name="test-hmp")  # pragma: no cover
