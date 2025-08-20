from pathlib import Path
from typing import Iterable, List

class LocalConnector:
    def __init__(self, roots: List[str], include: List[str] | None = None, exclude: List[str] | None = None):
        self.roots = [Path(r) for r in roots]
        self.include = include or ["**/*"]
        self.exclude = exclude or []

    def iter_files(self) -> Iterable[Path]:
        for root in self.roots:
            for pattern in self.include:
                for p in root.glob(pattern):
                    if not p.is_file():
                        continue
                    skip = any(p.match(x) for x in self.exclude)
                    if not skip:
                        yield p
