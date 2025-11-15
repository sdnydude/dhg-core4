# Changelog – DHG Core 4

All notable changes to this project will be documented in this file.

The format is based on [Semantic Versioning](./VERSIONING.md).

---

## [0.1.0] – Initial Vertical Slice

### Added
- FastAPI backend with `/assets` CRUD endpoints.
- PostgreSQL 16 with `vector` extension enabled via init script.
- React + Vite + TypeScript frontend to create and list assets.
- Docker Compose stack for local development:
  - `postgres`
  - `backend`
  - `frontend`
- Initial documentation set:
  - `README.md`
  - `ARCHITECTURE.md`
  - `DEVELOPMENT.md`
  - `INFRA.md`
  - `PRIMER.md`
  - `CONTRIBUTING.md`
  - `SECURITY.md`
  - `LICENSE` (MIT)
