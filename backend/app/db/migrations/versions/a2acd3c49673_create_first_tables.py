"""create_first_tables

Revision ID: a2acd3c49673
Revises: bc4b83c77749
Create Date: 2021-03-08 03:24:01.656795

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = 'a2acd3c49673'
down_revision = 'bc4b83c77749'
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
