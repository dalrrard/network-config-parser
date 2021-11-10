"""Compiled regex patterns for parsing IOS configuration sections.

These are internal interfaces and may change at any time.
"""
import re

hostname = re.compile(
    r"^hostname\s+(?P<hostname>[\w\d\-]+)$",
    re.MULTILINE,
)

version = re.compile(
    r"^version\s+(?P<version>[\d\.]+)$",
    re.MULTILINE,
)

banner = re.compile(
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
    re.MULTILINE | re.VERBOSE,
)

ipv4_address = re.compile(
    r"""\b(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.  # 0 - 255
          (25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.  # 0 - 255
          (25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.  # 0 - 255
          (25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])    # 0 - 255
          ((?:/)(3[0-2]|[12]?[0-9]|[0-9]))?         # /0-32
          \b""",
    re.MULTILINE | re.VERBOSE,
)

interfaces = re.compile(
    r"""
    ^(interface\s+?[\w/\.\-]+?\n
    .*?
    (?=^!))
    """,
    re.MULTILINE | re.VERBOSE | re.DOTALL,
)

interface = re.compile(
    r"""
    ^(interface\s+?(?P<interface_name>[\w/\.\-]+?)\n
    (?P<description>description\s+?(?P<description_value>.*?)\n)?
    (?P<interface_mode>switchport\s+?mode\s+?(?P<interface_mode_name>[\w\-]+?)\n)?
    (?P<interface_access_vlan>switchport\s+?access\s+?vlan\s+?(?P<interface_access_vlan_number>[\d\-]+?)\n)?
    (?P<interface_port_security>switchport\s+?port-security\s+?(?P<interface_port_security_name>[\w\-]+?)\n)?
    .*?
    (?=^!))
    """,
    re.MULTILINE | re.VERBOSE | re.DOTALL,
)
