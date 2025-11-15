# DHG Core 4 — Architecture

DHG Core 4 establishes the architectural foundation of the broader DHG ecosystem. This document details the system layout, service boundaries, runtime assumptions, and future expansions consistent with DHG’s multi-agent AI production architecture.

---

## 1. Architectural Principles

- **Simplicity first:** The vertical slice must be easy to run, debug, and extend.
- **Containerized environment:** All services run in Docker for consistency.
- **Postgres as source of truth:** All state, metadata, and future embeddings live in PostgreSQL.
- **Future-proofing:** Built to evolve into DHG’s full ingest, ASR, RAG, and studio pipeline.

---

## 2. System Components

### Backend (FastAPI)
Located in `backend/`.

Responsibilities:
- API serving.
- Asset CRUD operations.
- Database connectivity.
- ORM for future job queues, transcripts, embeddings.

---

### Frontend (React + Vite + TypeScript)
Located in `frontend/`.

Responsibilities:
- Operator-facing UI.
- Asset listing and creation.
- Extendable component system for future operator panels.

---

### Database (PostgreSQL 16 with pgvector)
Located via Docker container.

Responsibilities:
- Stores asset metadata.
- Provides vector indexing functionality.
- Ready for RAG expansion.

---

### Infrastructure (Docker Compose)
Located in `infra/`.

Responsibilities:
- Orchestrates the local development environment.
- Ensures reproducible deployments.
- Provides a path to future K8s/OpenStack migrations.

---

## 3. Data Model

The current minimal model includes:

### Asset
- `id`: UUID
- `title`: string
- `description`: string
- `kind`: video/clip/document
- `created_at`
- `updated_at`

Future fields:
- `org_id`
- `status`
- Transcript and segment tables
- Embeddings

---

## 4. Runtime Flow

1. Developer runs `docker compose up`.
2. Postgres boots and loads the vector extension.
3. Backend starts and auto-initializes schema.
4. Frontend starts and connects to backend.
5. User creates assets via UI.
6. Backend persists assets in Postgres.

---

## 5. Future Architecture Layers

- **Ingest worker container**  
- **MinIO object storage**  
- **Node-RED orchestration**  
- **ffmpeg pipeline**  
- **Whisper ASR**  
- **RAG + Embeddings**  
- **Studio OS integration**  
