# Employee Management API

A Python-based employee management API built with FastAPI.

## Current Status

- FastAPI application setup
- Health endpoint: `GET /health`
- Environment configuration using Pydantic Settings
- Automated health endpoint test
- Draft API contract
- Ten fictional employee records and referenced department records from the supplied LedgerForge Master Dataset

## Technologies

- Python 3.12
- FastAPI
- Uvicorn
- Pydantic Settings
- Pytest
- SQLAlchemy and Alembic (database integration planned)
- PostgreSQL and Docker Compose (setup and verification completed)

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
├── docker-compose.yml
├── Dockerfile
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

Note: The current health endpoint does not require a database connection. Docker Compose starts the FastAPI application and PostgreSQL database. The health endpoint and Swagger UI have been verified successfully.


## Run with Docker Compose

Make sure `.env` exists in the project root and contains the required local environment variables. You can create it by copying `.env.example` to `.env`.

Start the API and PostgreSQL database:

```bash
docker compose up --build
```

Once the services start, open:

- Health check: http://localhost:8000/health
- Swagger API documentation: http://localhost:8000/docs

Expected health response:

```json
{
  "status": "ok"
}
```

Stop the services with `Ctrl+C`, or run:

```bash
docker compose down
```

To remove the local PostgreSQL volume and its stored data as well, run `docker compose down -v`. Use this only when you intend to delete that data.

## Run Tests

```powershell
python -m pytest
```

## API Contract

See `docs/api-contract.md`. Employee, department, and team endpoints are planned and have not been implemented yet.

## Sample Data

The file `scripts/sample_employees.json` contains sample records sourced from the supplied **LedgerForge Master Dataset**.

- **Employees:** First 10 employee rows from the source dataset.
- **Departments:** Department records referenced by those employees.
- **Data format:** JSON.
- **Data:** Fictional training records; not real employee information.

The employee records preserve the source dataset's fields, including `employee_id`, `department_id`, `role_id`, `hire_date`, and `employment_status`.

The sample data has been validated for:
- Exactly 10 employee records.
- Unique employee IDs and work email addresses.
- Department references matching the included department records.

This file is sample data for development and review. It does not mean that employee database models or CRUD endpoints have been implemented.

## Planned Work

- [x] Complete Dockerfile and Docker Compose setup and verify API and PostgreSQL startup
- Implement employee, department, and role database models
- Add Alembic migrations and rollback verification
- Implement employee CRUD and team APIs
- Add repeatable seed scripts and CSV exports
- Share the API contract and sample dataset for review

## Security

- Keep `.env` out of Git.
- Commit `.env.example` with placeholder values only.
- Never commit real credentials or secret keys.

## Handoff package

- [Draft API Contract](docs/api-contract.md)
- [Sample Employee Dataset](scripts/sample_employees.json)

These files are provided for the Task 1 Day-2 handoff. The sample JSON contains 10 fictional employee records for reference.