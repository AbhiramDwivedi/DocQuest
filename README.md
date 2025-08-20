# DocQuest

Local-first, enterprise-grade document search with RAG + Knowledge Graph, built around MCP.

## What’s here
- `backend/`: FastAPI MCP server stubs
- `frontend/`: Next.js chat shell
- `docs/requirements.md` and `docs/plan.md`
- `docker-compose.yml`, `Makefile`
- `.github/workflows`: CI + PR LLM reviewer
- `.devcontainer/`: Codespaces-ready env
- `scripts/`: bootstrap

## Quickstart (Codespaces – cloud-only)
- Open this repo in Codespaces.
- Bring services up:
```bash
cp .env.example .env
make bootstrap
docker compose up -d --build
# Backend: http://localhost:8000/healthz
# Frontend: http://localhost:3000
```
