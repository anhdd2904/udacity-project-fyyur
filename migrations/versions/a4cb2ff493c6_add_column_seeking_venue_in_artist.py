"""add column seeking_venue in Artist

Revision ID: a4cb2ff493c6
Revises: 87d494ba3c08
Create Date: 2024-07-23 21:46:50.351790

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a4cb2ff493c6'
down_revision = '87d494ba3c08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seeking_venue', sa.String(length=2), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.drop_column('seeking_venue')

    # ### end Alembic commands ###
