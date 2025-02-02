"""Added Auditing table

Revision ID: c079e0f9d2a7
Revises: 96d78f29d81f
Create Date: 2019-10-21 10:43:37.458499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c079e0f9d2a7'
down_revision = '96d78f29d81f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auditing',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_auditing_created_date'), 'auditing', ['created_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_auditing_created_date'), table_name='auditing')
    op.drop_table('auditing')
    # ### end Alembic commands ###
