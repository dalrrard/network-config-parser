"""Test ios_parser."""
from typing import Union

import pytest

from ncp.ios import parser


class TestDepthTracker:
    """Test DepthTracker and PositiveInt descriptor."""

    def test_required_arguments(self) -> None:
        # pylint: disable=no-self-use
        """Test that arguments must be passed to DepthTracker."""
        with pytest.raises(TypeError):
            parser.DepthTracker()

    def test_current_depth_set_no_negative_numbers(self) -> None:
        # pylint: disable=no-self-use
        """Test that current_depth can't be changed to negative number."""
        tracker = parser.DepthTracker(current_depth=0, last_node=0)
        with pytest.raises(ValueError):
            tracker.current_depth = -1

    def test_last_node_set_no_negative_numbers(self) -> None:
        # pylint: disable=no-self-use
        """Test that last_node can't be changed to negative number."""
        tracker = parser.DepthTracker(current_depth=0, last_node=0)
        with pytest.raises(ValueError):
            tracker.last_node = -1

    def test_current_depth_init_no_negative_numbers(self) -> None:
        # pylint: disable=no-self-use
        """Test that current_depth can't be initialized to negative number."""
        with pytest.raises(ValueError):
            parser.DepthTracker(current_depth=-1, last_node=0)

    def test_last_node_init_no_negative_numbers(self) -> None:
        # pylint: disable=no-self-use
        """Test that last_node can't be initialized to negative number."""
        with pytest.raises(ValueError):
            parser.DepthTracker(current_depth=0, last_node=-1)

    @pytest.mark.parametrize(
        "test_input, expected",
        [
            (1, 1),
            pytest.param("a", "a", marks=pytest.mark.xfail(raises=TypeError)),
        ],
    )
    def test_get_only_ints(
        self,
        test_input: Union[str, int],
        expected: Union[str, int],
    ) -> None:
        # pylint: disable=no-self-use
        """Test that only ints can be retrieved from current_depth."""
        tracker = parser.DepthTracker(current_depth=0, last_node=0)
        # pylint: disable=protected-access
        tracker._current_depth = test_input  # type: ignore[attr-defined]
        assert tracker.current_depth == expected


class TestIOSParser:
    """Test IOSParser class."""

    def test_ios_parser_initialization(self, ios_parser: parser.IOSParser) -> None:
        # pylint: disable=no-self-use
        """Test IOSParser initialization returns correct type."""
        assert isinstance(ios_parser, parser.IOSParser)

    def test_get_hostname(self, ios_parser: parser.IOSParser) -> None:
        # pylint: disable=no-self-use
        """Test that hostname is parsed from the configuration file correctly."""
        assert ios_parser.hostname == "DSW"
