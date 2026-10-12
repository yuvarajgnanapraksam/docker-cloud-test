
# Employee Management API

A beginner-friendly employee management API built with Python and FastAPI.

## Current Features

- Health check endpoint
- Automatic API documentation
- Environment-based configuration
- Automated health-check test
- Sample JSON data containing 10 fictional employees

## Technologies

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic Settings
- Pytest

## Project Structure

```text
employee-management-api/
├── app/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── main.py
│   └── config.py
├── tests/
│   └── test_health.py
├── scripts/
│   └── sample_employees.json
├── docs/
│   └── api-contract.md
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## Local Setup

### 1. Create and activate a virtual environment

```bash
py -3.12 -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```bash
pip install fastapi "uvicorn[standard]" pydantic-settings pytest httpx
```

### 3. Run the application

```bash
python -m uvicorn app.main:app --reload
```

Health check: http://127.0.0.1:8000/health

API documentation: http://127.0.0.1:8000/docs

## Run Tests

```bash
python -m pytest
```

## Sample Data

Fictional employee records are available in:

`scripts/sample_employees.json`

## Planned Work

- PostgreSQL integration with Docker Compose
- Employee, department, and role data models
- Database migrations
- Employee management endpoints
- Data seeding and CSV exports

## Security

- Keep `.env` out of version control.
- Use `.env.example` as a configuration template.
- Never commit real credentials or secret keys.
