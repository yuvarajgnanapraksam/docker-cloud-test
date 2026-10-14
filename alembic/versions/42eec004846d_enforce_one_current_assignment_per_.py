
"""enforce one current assignment per employee

Revision ID: 42eec004846d
Revises: d2bf57b46e06
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "42eec004846d"
down_revision: Union[str, Sequence[str], None] = "d2bf57b46e06"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_index(
        "uq_employee_assignments_current_per_employee",
        "employee_assignments",
        ["employee_id"],
        unique=True,
        postgresql_where=sa.text("effective_to IS NULL"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(
        "uq_employee_assignments_current_per_employee",
        table_name="employee_assignments",
    )
