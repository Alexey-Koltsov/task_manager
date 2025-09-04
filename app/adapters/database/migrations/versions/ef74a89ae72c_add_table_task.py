"""add table task

Revision ID: ef74a89ae72c
Revises: 
Create Date: 2025-09-02 14:17:25.207929

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ef74a89ae72c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table('task',
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status', sa.Enum('created', 'in_work', 'finished', name='statusenum'), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('task')
