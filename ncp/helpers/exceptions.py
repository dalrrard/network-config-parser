"""Define project exceptions."""


class Error(Exception):
    """Base class for all exceptions raised by this module."""


class FileError(Exception):
    """Exception for low-level file issues."""


class ParseError(Error):
    """Exception for all configuration parsing issues."""


class SectionNotFoundError(ParseError):
    """Exception for unfound configuration sections."""
