## Todo FastAPI

Todo FastAPI is a small full‑stack example with a FastAPI backend, PostgreSQL (via Tortoise ORM and Aerich), and a React (Vite) frontend. It’s meant to be easy to spin up, explore, and tear down.

### Run the stack with Docker

- **Start services**: `docker compose up -d --build`
- **Stop services**: `docker compose down`

### Backend database & migrations

- **Init databases**: the `backend/db/create.sql` script creates `backend_dev` and `backend_test` in Postgres.
- **Run Aerich inside the backend container** (after `docker compose up -d --build`):
  - `docker compose exec backend uv run aerich init-db`
  - `docker compose exec backend uv run aerich migrate`
  - `docker compose exec backend uv run aerich upgrade`

### Inspect PostgreSQL

- **Open psql inside the DB container** (example):  
  `docker exec -it todo-fastapi-backend-db-1 psql -U postgres`
- **List databases**: `\l`
- **Connect to dev DB**: `\c backend_dev`
- **List tables**: `\dt`

### Frontend (React / Vite)

From the `frontend` folder:

- **Install deps (first time)**: `npm install`
- **Start dev server**: `npm run dev`

### URLs

- **FastAPI docs (Swagger)**: `http://localhost:8004/docs`
- **Todo app (Vite dev server)**: `http://localhost:5173`
