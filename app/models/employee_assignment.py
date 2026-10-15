from datetime import date, datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Date,
    DateTime,
    ForeignKey,
    Index,
    Integer,
    String,
    func,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.employee import Employee

class EmployeeAssignment(Base):
    __tablename__ = "employee_assignments"
	
        
    __table_args__ = (
        CheckConstraint(
            "effective_to IS NULL OR effective_to >= effective_from",
            name="effective_to_gte_effective_from",
        ),
        Index(
            "uq_employee_assignments_current_per_employee",
            "employee_id",
            unique=True,
            postgresql_where=text("effective_to IS NULL"),
        ),
    )

    assignment_id: Mapped[str] = mapped_column(String(50), primary_key=True)

    employee_id: Mapped[str] = mapped_column(
        String(50),
        ForeignKey("employees.employee_id"),
        nullable=False,
        index=True,
    )
    effective_from: Mapped[date] = mapped_column(Date, nullable=False)
    effective_to: Mapped[date | None] = mapped_column(Date)

    department_id: Mapped[str | None] = mapped_column(
        String(50),
        ForeignKey("departments.department_id"),
    )
    role_id: Mapped[str | None] = mapped_column(
        String(50),
        ForeignKey("roles.role_id"),
    )
    job_level: Mapped[int | None] = mapped_column(Integer)
    manager_id: Mapped[str | None] = mapped_column(
        String(50),
        ForeignKey("employees.employee_id"),
    )
    change_reason: Mapped[str | None] = mapped_column(String(255))

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )
    is_active: Mapped[bool] = mapped_column(
    Boolean,
    nullable=False,
    server_default="true",
    )
    employee: Mapped["Employee"] = relationship(
        foreign_keys=[employee_id],
    )
    manager: Mapped["Employee | None"] = relationship(
        foreign_keys=[manager_id],
    )
