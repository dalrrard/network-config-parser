"""Test ios_parser."""
from ncp.ios import parser


class TestDepthTracker:
    def test_default_values(self) -> None:
        tracker = parser.DepthTracker(0, 0)
        assert (tracker.current_depth, tracker.last_node) == (0, 0)
