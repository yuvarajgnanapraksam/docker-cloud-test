
from decimal import Decimal

from sqlalchemy import ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


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

    department: Mapped["Department"] = relationship(back_populates="roles")
    employees: Mapped[list["Employee"]] = relationship(back_populates="role")
