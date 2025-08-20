from typing import Any, Dict

class ContentPlugin:
    async def search(self, query: str, top_k: int = 8) -> Dict[str, Any]:
        return {"answer": "(content stub)", "citations": []}

class MetadataPlugin:
    async def filter(self, filters: Dict[str, Any]) -> Dict[str, Any]:
        return {"rows": []}

class GraphPlugin:
    async def cypher(self, query: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
        return {"nodes": [], "edges": []}
