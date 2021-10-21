"""Create fixtures for IOS parser tests."""
from pathlib import Path
from typing import Iterable

import pytest

from ncp.ios import parser

pytest_plugins = "pytester"  # pylint: disable=invalid-name


@pytest.fixture
def rootdir() -> Path:
    """Get root directory for IOS parser tests.

    Returns
    -------
    Path
        Parent folder of IOS parser tests.
    """
    # request.startpath
    return Path(__file__).resolve(strict=True).parent


# pylint: disable=redefined-outer-name
@pytest.fixture
def ios_parser(rootdir: Path) -> Iterable[parser.IOSParser]:
    """Get ios config files used for testing.

    Parameters
    ----------
    rootdir : Path
        Parent directory of IOS parser tests from the `rootdir` fixture.

    Yields
    ------
    parser.IOSParser
        IOSParser object that represents the parsed IOS configuration file.
    """
    ios_config = parser.IOSParser(config=rootdir / "data" / "config.cfg")
    yield ios_config
    del ios_config
