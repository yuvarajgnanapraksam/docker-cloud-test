"""add assignment date constraint

Revision ID: d2bf57b46e06
Revises: 8b725ca9b2a5
Create Date: 2026-10-14 10:49:06.928023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2bf57b46e06'
down_revision: Union[str, Sequence[str], None] = '8b725ca9b2a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint(
        "effective_to_gte_effective_from",
        "employee_assignments",
        "effective_to IS NULL OR effective_to >= effective_from",
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(
        "effective_to_gte_effective_from",
        "employee_assignments",
        type_="check",
    )
