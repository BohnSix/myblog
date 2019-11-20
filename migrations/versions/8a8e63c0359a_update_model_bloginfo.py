"""update Model BlogInfo

Revision ID: 8a8e63c0359a
Revises: 
Create Date: 2019-11-20 22:15:42.151947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a8e63c0359a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogInfo', sa.Column('selfIntro', sa.String(length=64), nullable=True))
    op.drop_column('blogInfo', 'navbar')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogInfo', sa.Column('navbar', sa.VARCHAR(length=64), nullable=True))
    op.drop_column('blogInfo', 'selfIntro')
    # ### end Alembic commands ###