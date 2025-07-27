"""Controller for handling CLI presentation logic."""

from __future__ import annotations

import logging

from rich.console import Console

from .services import ProfileService

logger = logging.getLogger(__name__)
console = Console()


class IntroController:
    """Controller orchestrating profile output."""

    def __init__(self) -> None:
        self.service = ProfileService()

    def display_profile(self) -> None:
        """Render profile information to the console."""
        ascii_name = self.service.ascii_name()
        profile = self.service.profile_text()
        console.print(ascii_name, style="bold magenta")
        console.print(profile, style="green")
