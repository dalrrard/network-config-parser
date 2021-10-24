"""Miscellaneous utilities."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


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
