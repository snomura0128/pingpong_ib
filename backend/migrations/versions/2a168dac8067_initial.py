"""initial

Revision ID: 2a168dac8067
Revises: 
Create Date: 2021-03-07 22:56:49.694631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a168dac8067'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('facilities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('ward_id', sa.String(length=2), nullable=False),
    sa.Column('image_url', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('facility_id', sa.Integer(), nullable=False),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wards',
    sa.Column('id', sa.String(length=2), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wards')
    op.drop_table('users')
    op.drop_table('favorites')
    op.drop_table('facilities')
    # ### end Alembic commands ###