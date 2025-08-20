# DocQuest – Requirements (v0.1)

- **Local-first** initial release; optional AWS+OSS tests later.
- **MCP** backend (Python FastAPI) + **Next.js** MCP client.
- **No AuthN/AuthZ initially**; Phase 1: SSO (OIDC/SAML) + RBAC.
- **Data residency**: local only initially; AWS (US) later.
- **LLMs**: OpenAI API and OSS/local mandatory; others optional via LiteLLM router.
- **Email sources**: EML/MSG files; no live mailbox integrations.
- **File streaming**: initial = analysis/paths; Phase 1 = previews & downloads.
- **Scale**: hundreds of files, ~1 TPS, few-seconds latency.

### Capabilities
- Ingestion via local connector; processors for PDF/DOCX/PPTX/XLSX/CSV/EML/MSG/Images/Mermaid/Structurizr.
- Image OCR+captioning; stock-image classifier to ignore stock-ish images; keep diagrams.
- Entity recognition + KG (Neo4j) with alias clustering and provenance.
- Hybrid retrieval (BM25 + pgvector embeddings) with optional re-ranker.
- Orchestrator (plan/parallelize/reflect); plugins: Content/Metadata/Graph.
- Responses show citations; clear split: **private doc** vs **public/LLM** knowledge.
- MCP transports: stdio (CLI/dev) + HTTP/WS (web) at initial launch.
- Logging levels selectable; OSS monitoring (Prometheus/Grafana/Otel) in Phase 1.
