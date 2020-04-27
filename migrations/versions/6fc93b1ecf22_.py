"""empty message

Revision ID: 6fc93b1ecf22
Revises: 834b1a697901
Create Date: 2018-07-28 16:24:57.433374

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6fc93b1ecf22'
down_revision = '834b1a697901'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('job',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=140), nullable=True),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('user', sa.Column('age', sa.String(length=10), nullable=True))
    op.add_column('user', sa.Column('height', sa.String(length=10), nullable=True))
    op.add_column('user', sa.Column('start_job', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('weight', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'weight')
    op.drop_column('user', 'start_job')
    op.drop_column('user', 'height')
    op.drop_column('user', 'age')
    op.drop_table('job')
    # ### end Alembic commands ###
