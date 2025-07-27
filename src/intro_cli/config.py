"""Configuration handling for intro_cli package."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    """Application configuration loaded from environment variables."""

    developer_name: str = os.getenv("DEVELOPER_NAME", "Unknown Developer")
    description: str = os.getenv("DEVELOPER_DESCRIPTION", "Python developer")
    contact: str = os.getenv("DEVELOPER_CONTACT", "N/A")


CONFIG = AppConfig()
