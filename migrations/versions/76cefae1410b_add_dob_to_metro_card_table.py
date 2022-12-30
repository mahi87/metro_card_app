"""add dob to metro_card table

Revision ID: 76cefae1410b
Revises: e951cac66f25
Create Date: 2022-12-31 01:14:02.515255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76cefae1410b'
down_revision = 'e951cac66f25'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('metro_card', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dob', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('metro_card', schema=None) as batch_op:
        batch_op.drop_column('dob')

    # ### end Alembic commands ###
