"""Parse network configuration files."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional, Union

from ncp.helpers import exceptions

from ..helpers import _patterns

# import networkx as nx


class PositiveInt(int):
    """Validate that integers >= 0."""

    def __set_name__(self, owner: object, name: str) -> None:
        """Add private attribute to calling class."""
        # pylint: disable=attribute-defined-outside-init
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj: object, objtype: Optional[DepthTracker] = None) -> int:
        """Get attribute."""
        if not isinstance(value := getattr(obj, self.private_name), int):
            raise TypeError(f"Expected an int: Got {value!r}")
        return value

    def __set__(self, obj: object, value: int) -> None:
        """Verify that attribute >= 0 and set it."""
        if value < 0:
            raise ValueError(
                f"Expected {self.public_name!r} to be at least 0: Got {value!r}"
            )
        setattr(obj, self.private_name, value)


@dataclass
class DepthTracker:
    """Keep state of nodes as we traverse the configuration."""

    current_depth: int = PositiveInt()
    last_node: int = PositiveInt()


@dataclass
class Config:
    """TODO."""


@dataclass
class IOSConfig:
    """IOSConfig class.

    Returns
    -------
    [type]
        [description]

    Raises
    ------
    exceptions.Error
        [description]
    exceptions.SectionNotFoundError
        [description]
    """

    config: Union[Path, str]
    _raw_config: str = field(init=False, repr=False)
    hostname: Optional[str] = field(init=False, repr=False)
    version: Optional[str] = field(init=False, repr=False)
    banner: Optional[dict[str, str]] = field(init=False, repr=False)
    parsed_config: Config = field(default_factory=Config, repr=False)

    def __post_init__(self) -> None:
        """Load variables after __init__."""
        self.config = Path(self.config)
        self._raw_config = self._load_config()
        try:
            self.hostname = self._get_hostname()
        except exceptions.SectionNotFoundError:
            self.hostname = None
        try:
            self.version = self._get_version()
        except exceptions.SectionNotFoundError:
            self.version = None
        try:
            self.banner = self._get_banner()
        except exceptions.SectionNotFoundError:
            self.banner = None

    def __str__(self) -> str:
        """Return string representation."""
        return f"Hostname: {self.hostname}\nFile: {self.config}"

    def _load_config(self) -> str:
        try:
            with open(self.config, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError as exc:
            raise exceptions.Error(f"File not found: {self.config}") from exc

    def _get_hostname(self) -> str:
        match = _patterns.hostname.search(self._raw_config)
        if not isinstance(match, re.Match):
            raise exceptions.SectionNotFoundError(
                "Section 'hostname' not found in configuration."
            )
        return match.group("hostname")

    def _get_version(self) -> str:
        match = _patterns.version.search(self._raw_config)
        if not isinstance(match, re.Match):
            raise exceptions.SectionNotFoundError(
                "Section 'version' not found in configuration."
            )
        return match.group("version")

    def _get_banner(self) -> Optional[dict[str, str]]:
        if match := _patterns.banner.findall(self._raw_config):
            return {banner_type: banner_text for banner_type, _, banner_text in match}
        return None

    def _split_sections(self) -> None:
        pass
