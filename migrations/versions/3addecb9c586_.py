"""empty message

Revision ID: 3addecb9c586
Revises: f1d57ae809db
Create Date: 2019-07-10 16:56:47.467063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3addecb9c586'
down_revision = 'f1d57ae809db'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('headteachers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('age', sa.INTEGER(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('headteachers')
    # ### end Alembic commands ###