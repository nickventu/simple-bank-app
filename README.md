# Simple Bank App

A full-stack banking application: users register and log in, open accounts, make deposits and withdrawals, and view transaction history. The backend is a REST API built with FastAPI and MySQL, secured with JWT authentication and per-account authorization. The frontend is a React single-page app.

## Features

- Register a user and log in with a hashed password (bcrypt)
- JWT authentication on every account route
- Ownership checks: a logged-in user can only read or change their own accounts (403 otherwise)
- Create accounts, deposit, withdraw, and view transaction history
- Input validation and clear 400/404 error responses

## Tech stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI, Uvicorn |
| Database | MySQL, SQLAlchemy ORM |
| Auth | JWT (python-jose), bcrypt |
| Frontend | React, Vite, React Router |

## Project structure

```
backend/
  app/
    main.py          # App setup and router registration
    database.py      # Engine and session setup
    models/          # SQLAlchemy models (User, Account, Transaction)
    schemas/         # Pydantic request/response schemas
    routers/         # HTTP routes (accounts, auth, users)
    services/        # Business logic (accounts, auth, users)
frontend/
  src/
    api.js           # Fetch helper that attaches the JWT
    pages/           # Home, Login, CreateAccount, AccountDetails,
                     # Deposit, Withdraw, TransactionHistory
```

The backend is layered: routes handle HTTP, services hold the business logic, and models and schemas define the data.

## API

All routes are served under `/api`. Interactive docs are at `http://localhost:8000/docs` when the backend is running.

| Method | Path | Auth | Description |
|---|---|---|---|
| POST | `/api/users` | No | Create a user |
| POST | `/api/auth/login` | No | Log in and receive a JWT |
| POST | `/api/accounts` | Yes | Create an account for the logged-in user |
| GET | `/api/accounts/{id}` | Yes | Get account details |
| POST | `/api/accounts/{id}/deposit` | Yes | Deposit funds |
| POST | `/api/accounts/{id}/withdraw` | Yes | Withdraw funds |
| GET | `/api/accounts/{id}/transactions` | Yes | List an account's transactions |

Authenticated requests send the token as `Authorization: Bearer <token>`.

## Getting started

### Prerequisites

- Python 3.12
- Node.js 18+
- A MySQL database

### Backend

```bash
# from the repository root
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt

copy .env.example .env          # Windows (use cp on macOS / Linux), then fill in your values

cd backend
uvicorn app.main:app --reload
```

The API runs at `http://localhost:8000`.

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open the address Vite prints (usually `http://localhost:5173`). The dev server proxies `/api` requests to the backend on port 8000.

### Environment variables

Defined in `.env` (see `.env.example`):

| Variable | Description |
|---|---|
| `DB_USER` | MySQL username |
| `DB_PASSWORD` | MySQL password |
| `DB_HOST` | MySQL host |
| `DB_PORT` | MySQL port (defaults to 3306) |
| `DB_NAME` | Database name |
| `JWT_SECRET_KEY` | Secret used to sign tokens. Generate one with `python -c "import secrets; print(secrets.token_hex(32))"` |

Never commit `.env`. It is listed in `.gitignore`.

## Build stages

The project was built in four stages, each preserved on its own branch:

| Branch | Stage |
|---|---|
| `v1-no-db` | REST API with in-memory storage |
| `v2-with-db` | MySQL persistence with SQLAlchemy |
| `v3-react-frontend` | React frontend |
| `v4-auth` | JWT authentication and authorization (merged into `main`) |

## Notes

- Passwords are hashed with bcrypt directly rather than through passlib, which has a compatibility issue with recent bcrypt releases.
- Authorization is enforced in the API: each account route checks that the account belongs to the user identified by the token.
