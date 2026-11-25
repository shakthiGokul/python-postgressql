# TODO

## Explore later: real-world migration and deployment workflow

Goal: ship schema changes (e.g. adding `address` to customers) safely from laptop to production.

- [ ] **Neon environments**: create `dev`, `staging`, and `main` (production) branches; one `DATABASE_URL` per environment (local `.env`, platform env vars for the rest)
- [ ] **Git branching**: `develop` → deploys to staging, `main` → deploys to production
- [ ] **Hosting platform**: pick one (Render / Railway / Fly.io / other) and set its pre-deploy command to `alembic upgrade head`
- [ ] **CI on pull requests (GitHub Actions)**:
  - create a temporary Neon branch
  - run `alembic upgrade head`
  - run `alembic check` (fails if a model changed without a migration)
  - optional: `alembic downgrade -1` then `upgrade head` again
  - run tests, then delete the temporary branch
- [ ] **Practice "expand, then contract"**: add `address` as optional → backfill → make it required in a later deploy
- [ ] **Team rules**: no manual production schema changes; never edit an applied migration; resolve "multiple heads" with `alembic merge`
- [ ] **Large-table safety**: concurrent indexes, `lock_timeout`, Neon branch snapshot before risky migrations
- [ ] **Optional**: Dockerfile that includes `migrations/` and `alembic.ini`

## In progress / up next

- [ ] First migration: drop `customers` in Neon → `alembic revision --autogenerate -m "create customers table"` → review → `alembic upgrade head`
- [ ] Remove `Base.metadata.create_all` from the lifespan in `src/server/main.py`
- [ ] Customer endpoints: get one, replace (PUT), delete
- [ ] Fix iCloud hidden-file issue (move project off Desktop, or use a `.nosync` venv)

## Later topics

- [ ] Authentication: users table, password hashing, JWT access + refresh tokens, `get_current_user` dependency
- [ ] Client ID / secret (client credentials) if other services need to call the API
- [ ] Automated tests with pytest + FastAPI TestClient
