"""update relationship

Revision ID: f323aba683fb
Revises: 0c9eb24f221f
Create Date: 2024-07-19 23:17:47.024140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f323aba683fb'
down_revision = '0c9eb24f221f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shows', schema=None) as batch_op:
        batch_op.add_column(sa.Column('venue_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'venue', ['venue_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('shows', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('venue_id')

    # ### end Alembic commands ###
