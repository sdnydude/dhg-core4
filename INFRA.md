# DHG Core 4 — Infrastructure Documentation

This document describes the Docker-based infrastructure for DHG Core 4.

---

## 1. Overview

The `infra/` directory provides:

- docker-compose.yml
- .env.example
- PostgreSQL init scripts
- Service orchestration

This composition provides a stable environment for development.

---

## 2. Services

- **postgres**
  - Image: pgvector/pgvector:pg16
  - Initializes `vector` extension
- **backend**
  - Built from `../backend`
  - FastAPI app
- **frontend**
  - Built from `../frontend`
  - Vite dev server

---

## 3. Running the Stack

```
cd infra
cp .env.example .env
docker compose up --build
```

---

## 4. Resetting

To remove all containers and volumes:

```
docker compose down -v
```
