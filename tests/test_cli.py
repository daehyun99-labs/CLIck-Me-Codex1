"""Tests for intro_cli CLI application."""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest  # noqa: F401

from click.testing import CliRunner

from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from intro_cli.cli import cli

if TYPE_CHECKING:  # pragma: no cover
    from _pytest.capture import CaptureFixture  # noqa: F401
    from _pytest.fixtures import FixtureRequest  # noqa: F401
    from _pytest.logging import LogCaptureFixture  # noqa: F401
    from _pytest.monkeypatch import MonkeyPatch  # noqa: F401
    from pytest_mock.plugin import MockerFixture  # noqa: F401


def test_introduce_output() -> None:
    """It prints introduction without error."""
    runner = CliRunner()
    result = runner.invoke(cli, ["introduce"])
    assert result.exit_code == 0
    assert "Python developer" in result.output
