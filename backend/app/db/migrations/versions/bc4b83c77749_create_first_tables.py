"""create_first_tables

Revision ID: bc4b83c77749
Revises: 
Create Date: 2021-03-08 02:47:32.365445

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = 'bc4b83c77749'
down_revision = None
branch_labels = None
depends_on = None


def create_hedgehogs_table() -> None:
    op.create_table(
        "hedgehogs",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("color_type", sa.Text, nullable=False),
        sa.Column("age", sa.Numeric(10, 1), nullable=False),
    )


def upgrade() -> None:
    create_hedgehogs_table()


def downgrade() -> None:
    op.drop_table("hedgehogs")
