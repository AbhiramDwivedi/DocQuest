from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any

@dataclass
class ProcessResult:
    text: str
    metadata: Dict[str, Any]
    images: list[str]

class BaseProcessor:
    MIME_TYPES: tuple[str, ...] = ()

    def can_handle(self, mime: str) -> bool:
        return mime in self.MIME_TYPES

    def process(self, path: Path) -> ProcessResult:
        raise NotImplementedError
