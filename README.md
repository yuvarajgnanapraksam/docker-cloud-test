# Employee Management API

A Python-based employee management API built with FastAPI.

## Current Status

- FastAPI application setup
- Health endpoint: `GET /health`
- Environment configuration using Pydantic Settings
- Automated health endpoint test
- Draft API contract
- Ten fictional employee records in JSON format

## Technologies

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic Settings
- Pytest
- SQLAlchemy and Alembic (database integration planned)
- PostgreSQL and Docker Compose (setup and verification pending)

## Project Structure

```text
employee-management-api/
├── app/
│   ├── api/
│   │   └── health.py
│   ├── modules/
│   ├── services/
│   ├── config.py
│   └── main.py
├── docs/
│   └── api-contract.md
├── scripts/
│   └── sample_employees.json
├── tests/
│   └── test_health.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Local Setup

### 1. Create and activate a virtual environment

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and configure the values for your environment.

Never commit `.env` or real credentials to version control.

### 4. Run the API

```powershell
python -m uvicorn app.main:app --reload
```

Health endpoint: http://127.0.0.1:8000/health

API documentation: http://127.0.0.1:8000/docs

Note: The current health endpoint does not require a database connection. PostgreSQL and Docker Compose setup and verification are pending.

## Run Tests

```powershell
python -m pytest
```

## API Contract

See `docs/api-contract.md`. Employee, department, and team endpoints are planned and have not been implemented yet.

## Sample Data

`scripts/sample_employees.json` contains ten fictional employee records for development and testing.

## Planned Work

- Complete Dockerfile and Docker Compose setup and verify API and PostgreSQL startup
- Implement employee, department, and role database models
- Add Alembic migrations and rollback verification
- Implement employee CRUD and team APIs
- Add repeatable seed scripts and CSV exports
- Share the API contract and sample dataset for review

## Security

- Keep `.env` out of Git.
- Commit `.env.example` with placeholder values only.
- Never commit real credentials or secret keys.