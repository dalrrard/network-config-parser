from pathlib import Path
from typing import Optional, Union

class DepthTracker:
    def __init__(self, current_depth: int, last_node: int) -> None:
        self.current_depth: int
        self.last_node: int
        self._current_depth: int
        self._last_node: int

class IOSParser:
    def __init__(self, config: Union[Path, str]) -> None: ...
    _raw_config: str
    hostname: str
    # parsed_config: Config
    def __post_init__(self) -> None: ...
    def __str__(self) -> str: ...
    def _load_config(self) -> str: ...
    def _get_hostname(self) -> str: ...
    def _get_banner(self) -> Optional[dict[str, dict[str, str]]]: ...
    def _split_sections(self) -> None: ...