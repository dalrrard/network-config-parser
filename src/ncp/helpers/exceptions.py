"""Define project exceptions."""


class Error(Exception):
    """Base class for all exceptions raised by this module."""


class ParseError(Error):
    """Base class for all configuration parsing issues."""


class SectionNotFoundError(ParseError):
    """Base class for unfound configuration sections."""
