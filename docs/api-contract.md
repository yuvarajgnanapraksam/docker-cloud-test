# Employee Management API - Draft Contract

## Base URL
http://localhost:8000

## Implementation Status
Only `GET /health` is implemented in Task 1.
All employee, department, and team endpoints below are planned for later tasks.

## 1. Health Check
- Method: GET
- Endpoint: `/health`
- Success: 200 OK
- Response:
```json
{
  "status": "ok"
}
```

## 2. List Employees
- Method: GET
- Endpoint: `/employees`
- Planned in: Task 3
- Query parameters:
  - `page`: page number, default 1
  - `size`: items per page, default 20
  - `department`: optional department filter
  - `q`: optional employee-name search
- Success: 200 OK
- Response: items, total count, page, and size

## 3. Get Employee
- Method: GET
- Endpoint: `/employees/{employee_id}`
- Planned in: Task 3
- Success: 200 OK
- Error: 404 Not Found if the employee does not exist

## 4. Create Employee
- Method: POST
- Endpoint: `/employees`
- Planned in: Task 3
- Request fields: name, work_email, department_id, role_id, joining_date
- Success: 201 Created
- Errors: 422 Validation Error; 409 Conflict for duplicate work email

## 5. Update Employee
- Method: PATCH
- Endpoint: `/employees/{employee_id}`
- Planned in: Task 3
- Request: fields to update
- Success: 200 OK
- Errors: 404 Not Found; 422 Validation Error; 409 Conflict for duplicate work email

## 6. Delete Employee
- Method: DELETE
- Endpoint: `/employees/{employee_id}`
- Planned in: Task 3
- Behaviour: soft-delete by setting `is_active` to false
- Success: 204 No Content
- Error: 404 Not Found if the employee does not exist

## 7. List Departments
- Method: GET
- Endpoint: `/departments`
- Planned in: Task 3
- Success: 200 OK
- Response: list of departments

## 8. List Department Employees
- Method: GET
- Endpoint: `/departments/{department_id}/employees`
- Planned in: Task 3
- Success: 200 OK
- Error: 404 Not Found if the department does not exist

## 9. Get Employee Team
- Method: GET
- Endpoint: `/employees/{employee_id}/team`
- Planned in: Task 3
- Purpose: list direct reports managed by the employee
- Success: 200 OK
- Error: 404 Not Found if the employee does not exist

## Common Error Format (Proposed)
```json
{
  "detail": "A clear error message"
}
```

## Notes
- Employee and department IDs will be defined by the database.
- Work email must be unique.
- Employee names must not be empty.
- Joining dates must not be in the future.
- Deleted employees are marked inactive rather than permanently removed.
- Final request and response schemas will be confirmed during implementation.
