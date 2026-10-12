
# Employee Management API — Draft Contract

## Base URL
http://localhost:8000

## 1. Health Check
- Method: GET
- Endpoint: /health
- Success: 200 OK
- Response:
  {"status": "ok"}

## 2. List Employees (Planned)
- Method: GET
- Endpoint: /employees
- Purpose: Retrieve employees with pagination and filters.

## 3. Get Employee (Planned)
- Method: GET
- Endpoint: /employees/{employee_id}
- Purpose: Retrieve one employee by ID.

## 4. Create Employee (Planned)
- Method: POST
- Endpoint: /employees
- Purpose: Create an employee record.

## 5. Update Employee (Planned)
- Method: PATCH
- Endpoint: /employees/{employee_id}
- Purpose: Update employee details.

## 6. Delete Employee (Planned)
- Method: DELETE
- Endpoint: /employees/{employee_id}
- Purpose: Soft-delete an employee.

Note: Only GET /health is implemented currently.
Other endpoints are planned and will be implemented in later tasks.
