
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.employee import Employee
    from app.models.role import Role


class Department(Base):
    __tablename__ = "departments"

    department_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    department_name: Mapped[str] = mapped_column(String(150), nullable=False)
    cost_center: Mapped[str | None] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, server_default="true", nullable=False
    )

    roles: Mapped[list["Role"]] = relationship(back_populates="department")
    employees: Mapped[list["Employee"]] = relationship(back_populates="department")
