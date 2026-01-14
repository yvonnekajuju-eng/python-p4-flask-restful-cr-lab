"""create db

Revision ID: 67f5d67aea55
Revises: 
Create Date: 2023-01-13 11:03:18.230084

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67f5d67aea55'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'plants',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('image', sa.String(255), nullable=True),
        sa.Column('price', sa.Float(), nullable=True)
    )


def downgrade():
    op.drop_table('plants')
