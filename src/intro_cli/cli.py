"""Command-line interface for the intro CLI application."""

from __future__ import annotations

import logging

import click

from .controllers import IntroController

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.group()
def cli() -> None:
    """CLI entry point."""


@cli.command()
def introduce() -> None:
    """Show the developer introduction."""
    IntroController().display_profile()


if __name__ == "__main__":
    cli()
