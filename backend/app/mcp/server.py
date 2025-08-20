# Placeholder for MCP server
from typing import Any, Dict

class MCPTarget:
    def list_tools(self) -> Dict[str, Any]:
        return {
            "ingest.run": {"description": "Run ingestion on a path", "input": {"path": "str"}},
            "search.content": {"description": "Hybrid RAG search", "input": {"query": "str"}},
        }

    async def ingest_run(self, path: str):
        return {"job_id": "stub-123", "path": path}

    async def search_content(self, query: str):
        return {"answer": "Stub answer", "citations": []}
