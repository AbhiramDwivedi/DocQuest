.PHONY: bootstrap backend.dev backend.test frontend.dev frontend.build
bootstrap:
	python3 -m venv .venv || true
	. .venv/bin/activate && pip install -e backend/[dev]
	cd frontend && npm i || true
backend.dev:
	. .venv/bin/activate && uvicorn app.main:app --reload --app-dir backend
backend.test:
	. .venv/bin/activate && pytest -q backend
backend.migrate:
	@echo "TODO: add alembic init/migrate"
frontend.dev:
	cd frontend && npm run dev
frontend.build:
	cd frontend && npm run build
