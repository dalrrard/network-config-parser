import re

from typing import Any, Optional, Union


class IOSParser:
    def __init__(self, config: str) -> None:
        self.config = str(config)
        self._raw_config = self._load_config()
        self.hostname = self._get_hostname()
        self.parsed_config = {}

    def __repr__(self) -> str:
        name = self.__class__.__name__
        return f"{name}({self.config!r})"

    def __str__(self) -> str:
        return f"Hostname: {self.hostname}\nFile: {self.config}"

    def _load_config(self) -> str:
        try:
            with open(self.config, "r") as file:
                return file.read()
        except FileNotFoundError:
            return self.config

    def _get_hostname(self) -> Optional[str]:
        if match := re.search(
            r"^hostname\s+(?P<hostname>.*)$",
            self._raw_config,
            re.MULTILINE,
        ):
            return match.group("hostname")
        return None

    def _get_banner(self) -> Optional[dict[str, dict[str, str]]]:
        if match := re.findall(
            r"""
            ^banner                     # Find lines beginning with "banner"
            \s+                         # Followed by one or more spaces
            (?P<banner_type>[\w\-]+)    # Capture banner type made of letters and dashes (login, motd, etc.)
            \s+                         # Followed by one or more spaces
            (?P<delimiter>[^\s]+)       # Followed by the delimiter made of one or more non-space characters (^C, #, etc.)
            $                           # Followed immediately by the end of the line
            (?s:                        # re.DOTALL - make dot match newlines inside the capture group
                (?P<banner_content>.*?) # Capture everything until the delimiter appears again
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


config = IOSParser("config.cfg")
