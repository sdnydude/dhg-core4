# DHG Core 4 — Security Documentation

DHG Core 4 is development-stage software but uses production-worthy patterns from day one.

---

## 1. Authentication & Authorization

Current vertical slice:
- No authentication.
- No authorization.

Future versions:
- JWT-based API access.
- Roles:
  - admin
  - producer
  - reviewer
  - viewer
- Multi-tenant scoping via `org_id`.

---

## 2. Database Security

- PostgreSQL runs in Docker.
- No sensitive PHI stored in this vertical slice.
- Future versions will use:
  - network isolation
  - access controls
  - encryption where applicable

---

## 3. Network Security

- Local-only Compose stack.
- Production deployments will require:
  - TLS
  - Reverse proxy (Traefik/Nginx)
  - Hardened Postgres config
  - Secrets vault

---

## 4. Disclosure

For private use only. Report any vulnerabilities directly to DHG leadership.
