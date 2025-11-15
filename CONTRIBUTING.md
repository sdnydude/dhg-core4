# Contributing to DHG Core 4

Thank you for contributing to the DHG platform.

---

## 1. Branching Strategy

- `main` — stable code.
- `feature/*` — new features.
- `fix/*` — bug fixes.
- `docs/*` — documentation only.

---

## 2. Commit Messages

Follow Conventional Commits:

- `feat: …`
- `fix: …`
- `docs: …`
- `chore: …`

---

## 3. Pull Requests

Each PR should include:

1. Summary of the change
2. Testing details
3. Risks or considerations
4. Linked issues (if any)

PRs should be small and focused.

---

## 4. Code Conventions

Backend:
- FastAPI + SQLAlchemy
- Pydantic models
- Type hints required

Frontend:
- React functional components
- TypeScript
- Clean separation of UI & API modules
