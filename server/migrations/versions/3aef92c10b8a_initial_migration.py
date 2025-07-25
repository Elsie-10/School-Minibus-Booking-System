"""Initial migration

Revision ID: 3aef92c10b8a
Revises: 
Create Date: 2025-07-24 11:31:31.806564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3aef92c10b8a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=40), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('routes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('route_name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('buses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('routeid', sa.Integer(), nullable=True),
    sa.Column('numberplate', sa.String(length=50), nullable=True),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['routeid'], ['routes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pickup_dropoff_locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name_location', sa.String(), nullable=True),
    sa.Column('GPSystem', sa.String(), nullable=True),
    sa.Column('routeid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['routeid'], ['routes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('bookings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bus_id', sa.Integer(), nullable=False),
    sa.Column('pickup_location', sa.String(), nullable=False),
    sa.Column('dropoff_location', sa.String(), nullable=False),
    sa.Column('seats_booked', sa.Integer(), nullable=False),
    sa.Column('booking_date', sa.Date(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['bus_id'], ['buses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bookings')
    op.drop_table('pickup_dropoff_locations')
    op.drop_table('buses')
    op.drop_table('users')
    op.drop_table('routes')
    op.drop_table('admin')
    # ### end Alembic commands ###
