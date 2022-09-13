"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Test Hm Python."""


if __name__ == "__main__":
    main(prog_name="test-hm-python")  # pragma: no cover
