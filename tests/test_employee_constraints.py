
from datetime import date

import pytest
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.db.session import engine
from app.models import Department, Employee, EmployeeAssignment, Role


@pytest.fixture
def db_session():
    with Session(engine) as session:
        yield session
        session.rollback()


def test_duplicate_work_email_is_rejected(db_session):
    department = Department(
        department_id="D_TEST",
        department_name="Test Department",
    )
    db_session.add(department)

    employee_1 = Employee(
        employee_id="E_TEST_1",
        first_name="Test",
        last_name="One",
        full_name="Test One",
        work_email="duplicate@example.com",
        hire_date=date(2026, 1, 1),
        employment_status="Active",
        department_id="D_TEST",
    )
    employee_2 = Employee(
        employee_id="E_TEST_2",
        first_name="Test",
        last_name="Two",
        full_name="Test Two",
        work_email="duplicate@example.com",
        hire_date=date(2026, 1, 2),
        employment_status="Active",
        department_id="D_TEST",
    )

    db_session.add_all([employee_1, employee_2])

    with pytest.raises(IntegrityError):
        db_session.flush()

    db_session.rollback()


def test_exit_date_before_hire_date_is_rejected(db_session):
    employee = Employee(
        employee_id="E_BAD_DATE",
        first_name="Test",
        last_name="Date",
        full_name="Test Date",
        work_email="bad-date@example.com",
        hire_date=date(2026, 5, 1),
        exit_date=date(2026, 4, 1),
        employment_status="Exited",
    )

    db_session.add(employee)

    with pytest.raises(IntegrityError):
        db_session.flush()

    db_session.rollback()


def test_assignment_end_before_start_is_rejected(db_session):
    department = Department(
        department_id="D_ASSIGN_TEST",
        department_name="Assignment Test",
    )
    role = Role(
        role_id="R_ASSIGN_TEST",
        department_id="D_ASSIGN_TEST",
        role_title="Test Role",
    )
    employee = Employee(
        employee_id="E_ASSIGN_TEST",
        first_name="Assign",
        last_name="Test",
        full_name="Assign Test",
        work_email="assign-test@example.com",
        hire_date=date(2026, 1, 1),
        employment_status="Active",
    )

    db_session.add_all([department, role, employee])
    db_session.flush()

    assignment = EmployeeAssignment(
        assignment_id="A_BAD_DATE",
        employee_id="E_ASSIGN_TEST",
        effective_from=date(2026, 6, 1),
        effective_to=date(2026, 5, 1),
        department_id="D_ASSIGN_TEST",
        role_id="R_ASSIGN_TEST",
    )
    db_session.add(assignment)

    with pytest.raises(IntegrityError):
        db_session.flush()

    db_session.rollback()


def test_employee_cannot_have_two_current_assignments(db_session):
    department = Department(
        department_id="D_CURRENT_TEST",
        department_name="Current Assignment Test",
    )
    role = Role(
        role_id="R_CURRENT_TEST",
        department_id="D_CURRENT_TEST",
        role_title="Current Test Role",
    )
    employee = Employee(
        employee_id="E_CURRENT_TEST",
        first_name="Current",
        last_name="Test",
        full_name="Current Test",
        work_email="current-test@example.com",
        hire_date=date(2026, 1, 1),
        employment_status="Active",
    )

    db_session.add_all([department, role, employee])
    db_session.flush()

    assignment_1 = EmployeeAssignment(
        assignment_id="A_CURRENT_1",
        employee_id="E_CURRENT_TEST",
        effective_from=date(2026, 1, 1),
        effective_to=None,
        department_id="D_CURRENT_TEST",
        role_id="R_CURRENT_TEST",
    )
    db_session.add(assignment_1)
    db_session.flush()

    assignment_2 = EmployeeAssignment(
        assignment_id="A_CURRENT_2",
        employee_id="E_CURRENT_TEST",
        effective_from=date(2026, 6, 1),
        effective_to=None,
        department_id="D_CURRENT_TEST",
        role_id="R_CURRENT_TEST",
    )
    db_session.add(assignment_2)

    with pytest.raises(IntegrityError):
        db_session.flush()

    db_session.rollback()
