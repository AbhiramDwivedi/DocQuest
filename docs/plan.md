# DocQuest – Plan & Milestones

## Milestones
- **M0 – Skeleton**: FastAPI + MCP tool stubs (stdio + WS/HTTP); Next.js chat shell; Postgres + pgvector; minimal RAG; logging; CI.
- **M1 – Ingestion**: parsers (PDF/DOCX/PPTX/XLSX/CSV/EML/MSG/Images/Mermaid/Structurizr); OCR+captioning + stock classifier; KG MVP (Neo4j).
- **M2 – Agentic Query**: orchestrator plan/parallel/reflect; Content/Metadata/Graph plugins; citations; private/public separation.
- **M3 – Phase 1 UX & Ops**: previews & downloads; feedback (👍/👎, pin) → re-rank; Prometheus/Grafana + Otel; basic audit; begin SSO/RBAC.

## Initial Issue Backlog
- Backend: FastAPI skeleton; MCP registry; models + Alembic; local connector; Processor base; PDF/EML/MSG parsers; OCR+caption; entity stub + KG writes; hybrid retrieval stub.
- Frontend: Chat shell + citations; Setup wizard → config.yaml; Jobs (ingestion status).
- CI/Tooling: ruff+mypy+pytest; Next build; PR LLM reviewer.
