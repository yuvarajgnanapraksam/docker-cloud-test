
from datetime import date, datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    UniqueConstraint,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.role import Role

class Employee(Base):
    __tablename__ = "employees"

    __table_args__ = (
        UniqueConstraint("work_email", name="uq_employees_work_email"),
        CheckConstraint(
            "exit_date IS NULL OR exit_date >= hire_date",
            name="exit_date_gte_hire_date",
        ),
        Index("ix_employees_full_name", "full_name"),
        Index("ix_employees_employment_status", "employment_status"),
    )

    employee_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    full_name: Mapped[str] = mapped_column(String(201), nullable=False)
    work_email: Mapped[str] = mapped_column(String(255), nullable=False)

    gender: Mapped[str | None] = mapped_column(String(30))
    date_of_birth: Mapped[date | None] = mapped_column(Date)
    hire_date: Mapped[date] = mapped_column(Date, nullable=False)
    exit_date: Mapped[date | None] = mapped_column(Date)
    employment_status: Mapped[str] = mapped_column(String(50), nullable=False)
    employment_type: Mapped[str | None] = mapped_column(String(50))

    department_id: Mapped[str | None] = mapped_column(
        String(50), ForeignKey("departments.department_id"), index=True
    )
    role_id: Mapped[str | None] = mapped_column(
        String(50), ForeignKey("roles.role_id"), index=True
    )
    manager_id: Mapped[str | None] = mapped_column(
        String(50), ForeignKey("employees.employee_id"), index=True
    )

    work_location: Mapped[str | None] = mapped_column(String(150))
    work_mode: Mapped[str | None] = mapped_column(String(50))
    highest_education: Mapped[str | None] = mapped_column(String(150))
    prior_experience_years: Mapped[Decimal | None] = mapped_column(Numeric(6, 2))
    career_gap_months: Mapped[int | None] = mapped_column(Integer)
    commute_distance_km: Mapped[Decimal | None] = mapped_column(Numeric(7, 2))
    pf_applicable: Mapped[str | None] = mapped_column(String(1))
    esi_applicable: Mapped[str | None] = mapped_column(String(1))
    notice_period_days: Mapped[int | None] = mapped_column(Integer)
    resignation_date: Mapped[date | None] = mapped_column(Date)
    exit_type: Mapped[str | None] = mapped_column(String(100))
    exit_reason: Mapped[str | None] = mapped_column(String(255))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, server_default="true"
    )

    department: Mapped["Department | None"] = relationship(
        back_populates="employees", foreign_keys=[department_id]
    )
    role: Mapped["Role | None"] = relationship(
        back_populates="employees", foreign_keys=[role_id]
    )
    manager: Mapped["Employee | None"] = relationship(
        "Employee",
        remote_side="Employee.employee_id",
        foreign_keys=[manager_id],
        back_populates="direct_reports",
    )

    direct_reports: Mapped[list["Employee"]] = relationship(
        "Employee",
        foreign_keys=[manager_id],
        back_populates="manager",
    )
