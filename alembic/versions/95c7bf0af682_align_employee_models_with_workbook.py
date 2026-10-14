
"""align employee models with workbook

Revision ID: 95c7bf0af682
Revises: 42eec004846d
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "95c7bf0af682"
down_revision: Union[str, Sequence[str], None] = "42eec004846d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "departments",
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.add_column(
        "departments",
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
    )
    op.add_column(
        "departments",
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
    )

    op.alter_column(
        "employee_assignments",
        "job_level",
        existing_type=sa.String(50),
        type_=sa.Integer(),
        existing_nullable=True,
        postgresql_using="NULLIF(job_level, '')::integer",
    )

    op.alter_column(
        "employees",
        "prior_experience_years",
        existing_type=sa.Integer(),
        type_=sa.Numeric(6, 2),
        existing_nullable=True,
        postgresql_using="prior_experience_years::numeric(6,2)",
    )
    op.alter_column(
        "employees",
        "commute_distance_km",
        existing_type=sa.Integer(),
        type_=sa.Numeric(7, 2),
        existing_nullable=True,
        postgresql_using="commute_distance_km::numeric(7,2)",
    )
    op.alter_column(
        "employees",
        "pf_applicable",
        existing_type=sa.Boolean(),
        type_=sa.String(1),
        existing_nullable=True,
        postgresql_using=(
            "CASE WHEN pf_applicable IS TRUE THEN 'Y' "
            "WHEN pf_applicable IS FALSE THEN 'N' ELSE NULL END"
        ),
    )
    op.alter_column(
        "employees",
        "esi_applicable",
        existing_type=sa.Boolean(),
        type_=sa.String(1),
        existing_nullable=True,
        postgresql_using=(
            "CASE WHEN esi_applicable IS TRUE THEN 'Y' "
            "WHEN esi_applicable IS FALSE THEN 'N' ELSE NULL END"
        ),
    )

    op.alter_column(
        "roles",
        "level",
        existing_type=sa.String(50),
        type_=sa.Integer(),
        existing_nullable=True,
        postgresql_using="NULLIF(level, '')::integer",
    )
    for column in (
        "band_min_annual",
        "band_mid_annual",
        "band_max_annual",
    ):
        op.alter_column(
            "roles",
            column,
            existing_type=sa.Numeric(12, 2),
            type_=sa.Numeric(14, 2),
            existing_nullable=True,
        )
    op.alter_column(
        "roles",
        "overtime_eligible",
        existing_type=sa.Boolean(),
        type_=sa.String(1),
        existing_nullable=True,
        postgresql_using=(
            "CASE WHEN overtime_eligible IS TRUE THEN 'Y' "
            "WHEN overtime_eligible IS FALSE THEN 'N' ELSE NULL END"
        ),
    )


def downgrade() -> None:
    op.alter_column(
        "roles",
        "overtime_eligible",
        existing_type=sa.String(1),
        type_=sa.Boolean(),
        existing_nullable=True,
        postgresql_using=(
            "CASE WHEN overtime_eligible = 'Y' THEN TRUE "
            "WHEN overtime_eligible = 'N' THEN FALSE ELSE NULL END"
        ),
    )
    for column in (
        "band_max_annual",
        "band_mid_annual",
        "band_min_annual",
    ):
        op.alter_column(
            "roles",
            column,
            existing_type=sa.Numeric(14, 2),
            type_=sa.Numeric(12, 2),
            existing_nullable=True,
        )
    op.alter_column(
        "roles",
        "level",
        existing_type=sa.Integer(),
        type_=sa.String(50),
        existing_nullable=True,
        postgresql_using="level::text",
    )

    op.alter_column(
        "employees",
        "esi_applicable",
        existing_type=sa.String(1),
        type_=sa.Boolean(),
        existing_nullable=True,
        postgresql_using=(
            "CASE WHEN esi_applicable = 'Y' THEN TRUE "
            "WHEN esi_applicable = 'N' THEN FALSE ELSE NULL END"
        ),
    )
    op.alter_column(
        "employees",
        "pf_applicable",
        existing_type=sa.String(1),
        type_=sa.Boolean(),
        existing_nullable=True,
        postgresql_using=(
            "CASE WHEN pf_applicable = 'Y' THEN TRUE "
            "WHEN pf_applicable = 'N' THEN FALSE ELSE NULL END"
        ),
    )
    op.alter_column(
        "employees",
        "commute_distance_km",
        existing_type=sa.Numeric(7, 2),
        type_=sa.Integer(),
        existing_nullable=True,
        postgresql_using="round(commute_distance_km)::integer",
    )
    op.alter_column(
        "employees",
        "prior_experience_years",
        existing_type=sa.Numeric(6, 2),
        type_=sa.Integer(),
        existing_nullable=True,
        postgresql_using="round(prior_experience_years)::integer",
    )

    op.alter_column(
        "employee_assignments",
        "job_level",
        existing_type=sa.Integer(),
        type_=sa.String(50),
        existing_nullable=True,
        postgresql_using="job_level::text",
    )

    op.drop_column("departments", "is_active")
    op.drop_column("departments", "updated_at")
    op.drop_column("departments", "created_at")
