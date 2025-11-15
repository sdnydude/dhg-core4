# DHG Core 4 — Development Guide

This guide describes how to develop, test, and extend the DHG Core 4 platform.

---

## 1. Prerequisites

- Docker & Docker Compose
- Node 20+
- Python 3.11+
- Ubuntu 24.04 (preferred for local dev)

---

## 2. Running Locally

```bash
cd infra
cp .env.example .env
docker compose up --build
```

This starts:
- Postgres (with pgvector)
- Backend (FastAPI)
- Frontend (Vite dev server)

---

## 3. Backend Development

### Run natively:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Code style:
- Pydantic for request/response models.
- SQLAlchemy 2.x style ORM.
- Use type hints everywhere.

---

## 4. Frontend Development

### Run natively:

```bash
cd frontend
npm install
npm run dev
```

### Code style:
- Functional React components
- TypeScript strict mode
- Vite module system
- Tailwind for styles (optional enhancement)

---

## 5. Testing

Future versions will add:
- `pytest` for backend tests.
- `vitest` or `jest` for frontend.
- Linting via `flake8`, `black`, ESLint, Prettier.

---

## 6. Branching Workflow

Recommended:

- `main` — always stable.
- `feature/*` — new features.
- `fix/*` — bug fixes.
- `docs/*` — documentation updates.

Example:

```bash
git checkout -b feature/add-org-id
```

Commit:

```bash
git commit -m "feat: add org_id field to asset model"
```
