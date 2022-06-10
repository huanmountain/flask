"""empty message

Revision ID: acd278ac6752
Revises: b00b2ca31d2b
Create Date: 2022-04-24 03:05:38.991839

"""

# revision identifiers, used by Alembic.
revision = 'acd278ac6752'
down_revision = 'b00b2ca31d2b'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('join_time', sa.DateTime(), nullable=True))
    op.drop_column('user', 'jion_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('jion_time', mysql.DATETIME(), nullable=True))
    op.drop_column('user', 'join_time')
    # ### end Alembic commands ###
