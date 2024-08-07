"""add gernes in Venue

Revision ID: d13e50b4dd49
Revises: a4cb2ff493c6
Create Date: 2024-07-24 00:43:36.726662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd13e50b4dd49'
down_revision = 'a4cb2ff493c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.drop_column('look_talent')

    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.String(length=120), nullable=True))
        batch_op.alter_column('look_talent',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=2),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.alter_column('look_talent',
               existing_type=sa.String(length=2),
               type_=sa.VARCHAR(length=100),
               existing_nullable=True)
        batch_op.drop_column('genres')

    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('look_talent', sa.VARCHAR(length=100), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
