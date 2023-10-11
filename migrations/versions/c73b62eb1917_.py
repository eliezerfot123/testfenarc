"""empty message

Revision ID: c73b62eb1917
Revises: 
Create Date: 2023-10-09 19:56:22.410939

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c73b62eb1917'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ElementsToProcess',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('idBulk', sa.Integer(), nullable=True),
    sa.Column('retries', sa.Integer(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ElementsToProcess')
    # ### end Alembic commands ###