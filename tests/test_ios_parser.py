"""Test ios_parser."""
from contextlib import contextmanager

import pytest

from ncp.ios import parser


@contextmanager
def does_not_raise():
    yield


class TestDepthTracker:
    def test_required_arguments(self) -> None:
        with pytest.raises(TypeError):
            parser.DepthTracker()

    def test_current_depth_set_no_negative_numbers(self) -> None:
        tracker = parser.DepthTracker(current_depth=0, last_node=0)
        with pytest.raises(ValueError):
            tracker.current_depth = -1

    def test_last_node_set_no_negative_numbers(self) -> None:
        tracker = parser.DepthTracker(current_depth=0, last_node=0)
        with pytest.raises(ValueError):
            tracker.last_node = -1

    def test_current_depth_init_no_negative_numbers(self) -> None:
        with pytest.raises(ValueError):
            parser.DepthTracker(current_depth=-1, last_node=0)

    def test_last_node_init_no_negative_numbers(self) -> None:
        with pytest.raises(ValueError):
            parser.DepthTracker(current_depth=0, last_node=-1)

    @pytest.mark.parametrize(
        "input, expectation",
        [
            (1, does_not_raise()),
            ("a", pytest.raises(TypeError)),
        ],
    )
    def test_get_only_ints(self, input, expectation) -> None:  # type: ignore
        tracker = parser.DepthTracker(current_depth=0, last_node=0)
        tracker._current_depth = input  # type: ignore
        with expectation:
            print(tracker)
