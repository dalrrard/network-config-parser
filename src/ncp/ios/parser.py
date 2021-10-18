"""Parse network configuration files."""
import re
from dataclasses import dataclass, field
from typing import Optional

from ncp.helpers import exceptions

# import networkx as nx


class PositiveInt(int):
    """Validate that integers >= 0."""

    def __set_name__(self, owner: object, name: str) -> None:
        """Add private attribute to calling class."""
        # pylint: disable=attribute-defined-outside-init
        self.public_name = name
        self.private_name = "_" + name

    def __get__(self, obj: object, objtype: Optional["DepthTracker"] = None) -> int:
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
class IOSParser:
    """IOSParser class.

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

    config: str
    _raw_config: str = field(init=False, repr=False)
    hostname: str = field(init=False, repr=False)
    parsed_config: Config = field(default_factory=Config, repr=False)

    def __post_init__(self) -> None:
        """Load variables after __init__."""
        self._raw_config = self._load_config()
        try:
            self.hostname = self._get_hostname()
        except exceptions.SectionNotFoundError:
            self.hostname = ""

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
        section = "hostname"
        match = re.search(
            fr"^{section}\s+(?P<{section}>.*)$",
            self._raw_config,
            re.MULTILINE,
        )
        if not isinstance(match, re.Match):
            raise exceptions.SectionNotFoundError(
                f"Section {section} not found in configuration."
            )
        return match.group(section)

    def _get_banner(self) -> Optional[dict[str, dict[str, str]]]:
        if match := re.findall(
            r"""
            ^banner                     # Find lines beginning with "banner"
            \s+                         # Followed by one or more spaces
            (?P<banner_type>[\w\-]+)    # Capture banner type made of letters and
                                        #       dashes (login, motd, etc.)
            \s+                         # Followed by one or more spaces
            (?P<delimiter>[^\s]+)       # Followed by the delimiter made of one or
                                        #       more non-space characters (^C, #, etc.)
            $                           # Followed immediately by the end of the line
            (?s:                        # re.DOTALL - make dot match newlines inside
                                        #       the capture group
                (?P<banner_content>.*?) # Capture everything until the delimiter
                                        #       appears again
                (?P=delimiter)
            )
            """,
            self._raw_config,
            re.MULTILINE | re.VERBOSE,
        ):
            return {
                "banner": {
                    banner_type: banner_text for banner_type, _, banner_text in match
                }
            }
        return None

    def _split_sections(self) -> None:
        pass
