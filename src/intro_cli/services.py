"""Service layer containing business logic for intro CLI."""

from __future__ import annotations

import logging
from dataclasses import dataclass

from pyfiglet import figlet_format

from .config import CONFIG

logger = logging.getLogger(__name__)


@dataclass
class ProfileService:
    """Service for building profile messages."""

    def ascii_name(self) -> str:
        """Return the developer name as ASCII art."""
        try:
            return figlet_format(CONFIG.developer_name)
        except Exception as exc:  # noqa: BLE001
            logger.exception("Failed generating ASCII art: %s", exc)
            return CONFIG.developer_name

    def profile_text(self) -> str:
        """Return a formatted profile text."""
        return f"{CONFIG.description}\nContact: {CONFIG.contact}"
