# DHG Core 4 — Platform Vertical Slice

DHG Core 4 is the foundation of the Digital Harmony Group (DHG) platform. It establishes the structural, architectural, operational, and development conventions that will scale into the full DHG CME Production OS, AI Pipeline, Studio OS, and Enterprise Platform.

This repository provides:

- A production-quality FastAPI backend service.
- A React + Vite + TypeScript frontend.
- PostgreSQL 16 with pgvector enabled for future embeddings and RAG.
- A clean Docker Compose development environment.
- A complete development workflow, documentation set, and GitHub automation.

DHG Core 4 is not a prototype. It is the first solid, stable, reproducible baseline for DHG’s AI and media pipeline stack.

---

## ✨ Capabilities

### Backend
- Asset model (videos, clips, documents).
- CRUD API for assets.
- SQLAlchemy-based ORM.
- Ready for future multi-tenancy (`org_id`) and processing pipelines.

### Frontend
- Asset listing UI.
- Asset creation UI.
- TypeScript-first interface design.
- Expandable component architecture for future operator tools.

### Infrastructure
- Docker-first environment.
- Postgres with pgvector enabled automatically.
- Backend + Frontend containers orchestrated cleanly.

---

## 📁 Repository Structure

```text
backend/     # FastAPI application
frontend/    # React + Vite + TypeScript UI
infra/       # Docker compose, env vars, DB init scripts
docs/        # Architecture, development, security, and platform documentation
```

---

## 🚀 Running Locally

```bash
cd infra
cp .env.example .env
docker compose up --build
```

Access:
- Backend API docs → http://localhost:8000/docs  
- Frontend Web UI → http://localhost:5173  

Stop:

```bash
docker compose down
```

Reset (including DB):

```bash
docker compose down -v
```

---

## 📘 Documentation

All DHG Core documentation is inside the `docs/` directory, including:

- Architecture  
- Security  
- Development workflow  
- Contributing guide  
- Versioning  
- Changelog  

---

## 🛣 Roadmap

Next milestones:

1. Add multi-tenancy (`org_id`).
2. Add job processing pipeline.
3. Add worker container.
4. Add MinIO for media storage.
5. Add Node-RED orchestration.
6. Add ffmpeg + Whisper ingest pipeline.
7. Add embeddings + RAG search service.

---

## 📄 License

The project is licensed under the MIT License (see `LICENSE`).
