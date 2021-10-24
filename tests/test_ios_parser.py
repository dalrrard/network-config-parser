"""Test ios_parser."""
# pylint: disable=no-self-use, protected-access
from pathlib import Path
from typing import Optional, Union

import pytest

import ncp.helpers.exceptions
from ncp.helpers import utils
from ncp.ios import parser


class TestDepthTracker:
    """Test DepthTracker and PositiveInt descriptor."""

    def test_required_arguments(self) -> None:
        """Test that arguments must be passed to DepthTracker."""
        with pytest.raises(TypeError):
            utils.DepthTracker()

    def test_current_depth_set_no_negative_numbers(self) -> None:
        """Test that current_depth can't be changed to negative number."""
        tracker = utils.DepthTracker(current_depth=0, last_node=0)
        with pytest.raises(ValueError):
            tracker.current_depth = -1

    def test_last_node_set_no_negative_numbers(self) -> None:
        """Test that last_node can't be changed to negative number."""
        tracker = utils.DepthTracker(current_depth=0, last_node=0)
        with pytest.raises(ValueError):
            tracker.last_node = -1

    def test_current_depth_init_no_negative_numbers(self) -> None:
        """Test that current_depth can't be initialized to negative number."""
        with pytest.raises(ValueError):
            utils.DepthTracker(current_depth=-1, last_node=0)

    def test_last_node_init_no_negative_numbers(self) -> None:
        """Test that last_node can't be initialized to negative number."""
        with pytest.raises(ValueError):
            utils.DepthTracker(current_depth=0, last_node=-1)

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
        """Test that only ints can be retrieved from current_depth."""
        tracker = utils.DepthTracker(current_depth=0, last_node=0)
        tracker._current_depth = test_input  # type: ignore[attr-defined]
        assert tracker.current_depth == expected


class TestIOSConfig:
    """Test IOSConfig class."""

    config_dir = Path(__file__).resolve(strict=True).parent / "data"

    def test_ios_parser_initialization(self) -> None:
        """Test IOSConfig initialization returns correct type."""
        path = self.config_dir / "config.cfg"
        hostname = "DSW"

        config = parser.IOSConfig(path)

        assert (
            isinstance(config, parser.IOSConfig)
            and str(config) == f"Hostname: {hostname}\nFile: {path}"
        )

    def test_ios_parser_initialization_bad_filename(self) -> None:
        """Test IOSConfig initialization with non-existent file fails."""
        with pytest.raises(ncp.helpers.exceptions.FileError):
            parser.IOSConfig(self.config_dir / "this_is_not_a_real_file")

    @pytest.mark.parametrize(
        "config, expected",
        [
            (parser.IOSConfig(config_dir / "config.cfg"), "DSW"),
            (parser.IOSConfig(config_dir / "config_no_hostname.cfg"), None),
        ],
    )
    def test_get_hostname(self, config: parser.IOSConfig, expected: str) -> None:
        """Test that hostname is parsed from the configuration file correctly."""
        assert config.hostname == expected

    @pytest.mark.parametrize(
        "config, expected",
        [
            (parser.IOSConfig(config_dir / "config.cfg"), "15.0"),
            (parser.IOSConfig(config_dir / "config_12-3.cfg"), "12.3"),
            (parser.IOSConfig(config_dir / "config_no_version.cfg"), None),
        ],
    )
    def test_get_version(self, config: parser.IOSConfig, expected: str) -> None:
        """Test that version is parsed from the configuration file correctly."""
        assert config.version == expected

    @pytest.mark.parametrize(
        "config, expected",
        [
            (
                parser.IOSConfig(config_dir / "config.cfg"),
                {
                    "login": (
                        "\nUNAUTHORIZED ACCESS TO THIS DEVICE IS PROHIBITED\nYou must"
                        " have explicit, authorized permission to access or configure"
                        " this device.\nUnauthorized attempts and actions to access or"
                        " use this system may result in civil and/or\ncriminal"
                        " penalties.\nAll activities performed on this device are"
                        " logged and monitored.\n"
                    ),
                    "motd": (
                        "\nMESSAGE OF THE DAY BANNER\nYou must have explicit,"
                        " authorized permission to access or configure this"
                        " device.\nUnauthorized attempts and actions to access or use"
                        " this system may result in civil and/or\ncriminal"
                        " penalties.\nAll activities performed on this device are"
                        " logged and monitored."
                    ),
                },
            ),
            (parser.IOSConfig(config_dir / "config_12-3.cfg"), None),
        ],
    )
    def test_get_banner(
        self, config: parser.IOSConfig, expected: Optional[dict[str, str]]
    ) -> None:
        """Test that banners are parsed from the configuration file correctly."""
        assert config.banner == expected

    def test_get_interfaces(self) -> None:
        """Test that interfaces are parsed from the configuration file correctly."""
        interfaces = parser.IOSConfig(self.config_dir / "config.cfg").interfaces
        interface_gb_0_2 = (
            "interface GigabitEthernet0/2\n"
            " switchport trunk encapsulation dot1q\n"
            " switchport trunk native vlan 998\n"
            " switchport trunk allowed vlan 1\n"
            " switchport mode trunk\n"
            " switchport nonegotiate\n"
            " spanning-tree portfast trunk\n"
            " ip dhcp snooping limit rate 75\n"
        )
        interface_pc_1 = (
            "interface Port-channel1\n"
            " switchport access vlan 1\n"
            " switchport mode access\n"
            " switchport port-security maximum 3\n"
            " switchport port-security violation restrict\n"
            " switchport port-security\n"
            " ip dhcp snooping trust\n"
        )
        interface_vlan_200 = "interface Vlan200\n ip address\n"
        assert (
            interfaces is not None
            and len(interfaces) == 75
            and interfaces[2] == interface_pc_1
            and interfaces[6] == interface_gb_0_2
            and interfaces[-1] == interface_vlan_200
        )

    def test_get_interfaces_no_interfaces(self) -> None:
        """Test that files are parsed correctly when there are no interfaces."""
        interfaces = parser.IOSConfig(
            self.config_dir / "config_no_interfaces.cfg"
        ).interfaces
        assert interfaces is None
