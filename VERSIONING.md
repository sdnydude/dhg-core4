# Versioning – DHG Core 4

DHG Core uses **Semantic Versioning**:

> **MAJOR.MINOR.PATCH**

- **MAJOR** – Breaking changes to public APIs or deployment shape.
- **MINOR** – Backward-compatible feature additions.
- **PATCH** – Backward-compatible bug fixes and small improvements.

---

## Mapping to DHG Phases

While the code uses semantic versioning, internal planning may reference DHG phases (0–5). A rough mapping:

- `0.x.y` – Early prototypes and vertical slices.
- `1.x.y` – Stable ingest, basic jobs, and media handling.
- `2.x.y` – RAG and knowledge features.
- `3.x.y` and above – Enterprise integrations and Studio OS alignment.

This is a guideline, not a strict rule; the authoritative version is always the semantic version string.

---

## Tagging

Each release should be tagged in git:

```bash
git tag -a v0.1.0 -m "Initial DHG Core vertical slice"
git push origin v0.1.0
```

---

## Pre-Release Versions

When needed, pre-releases may be used:

- `0.2.0-rc.1`
- `1.0.0-beta.1`

These indicate builds that are not yet considered fully stable for all use cases.
