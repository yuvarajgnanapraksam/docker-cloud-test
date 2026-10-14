from datetime import datetime
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.department import Department
    from app.models.employee import Employee

class Role(Base):
    __tablename__ = "roles"

    role_id: Mapped[str] = mapped_column(String(50), primary_key=True)
    department_id: Mapped[str] = mapped_column(
        String(50),
        ForeignKey("departments.department_id"),
        nullable=False,
        index=True,
    )
    role_title: Mapped[str] = mapped_column(String(150), nullable=False)
    level: Mapped[int | None] = mapped_column(Integer)
    grade: Mapped[str | None] = mapped_column(String(50))
    band_min_annual: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    band_mid_annual: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    band_max_annual: Mapped[Decimal | None] = mapped_column(Numeric(14, 2))
    overtime_eligible: Mapped[str | None] = mapped_column(String(1))
    band_year: Mapped[int | None] = mapped_column(Integer)

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
        Boolean, default=True, nullable=False
    )

    department: Mapped["Department"] = relationship(back_populates="roles")
    employees: Mapped[list["Employee"]] = relationship(back_populates="role")
