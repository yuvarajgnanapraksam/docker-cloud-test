
# LedgerForge — Employee Master ER Diagram

```mermaid
erDiagram
    DEPARTMENTS ||--o{ ROLES : contains
    DEPARTMENTS ||--o{ EMPLOYEES : has
    ROLES ||--o{ EMPLOYEES : assigned
    EMPLOYEES o|--o{ EMPLOYEES : manages
    EMPLOYEES ||--o{ EMPLOYEE_ASSIGNMENTS : has_history
    DEPARTMENTS o|--o{ EMPLOYEE_ASSIGNMENTS : assigned_to
    ROLES o|--o{ EMPLOYEE_ASSIGNMENTS : records

    DEPARTMENTS {
        string department_id PK
        string department_name
        string cost_center
        string description
        datetime created_at
        datetime updated_at
        boolean is_active
    }

    ROLES {
        string role_id PK
        string department_id FK
        string role_title
        integer level
        string grade
        decimal band_min_annual
        decimal band_mid_annual
        decimal band_max_annual
        string overtime_eligible
        integer band_year
        datetime created_at
        datetime updated_at
        boolean is_active
    }

    EMPLOYEES {
        string employee_id PK
        string work_email UK
        string department_id FK
        string role_id FK
        string manager_id FK
        date hire_date
        date exit_date
        string employment_status
        decimal prior_experience_years
        decimal commute_distance_km
        string pf_applicable
        string esi_applicable
        datetime created_at
        datetime updated_at
        boolean is_active
    }

    EMPLOYEE_ASSIGNMENTS {
        string assignment_id PK
        string employee_id FK
        string department_id FK
        string role_id FK
        string manager_id FK
        date effective_from
        date effective_to
        integer job_level
        datetime created_at
        datetime updated_at
        boolean is_active
    }
```

## Relationship summary

- One department can have multiple roles and employees.
- An employee can report to another employee through `manager_id`.
- `employee_assignments` stores role and department assignment history.
- `work_email` must be unique.
- An employee's current assignment is intended to have no `effective_to` date.
- `is_active` supports soft deletion instead of physically deleting records.
