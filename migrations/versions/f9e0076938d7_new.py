"""new

Revision ID: f9e0076938d7
Revises: 
Create Date: 2019-10-17 21:29:42.962693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9e0076938d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Clinics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Users_email'), 'Users', ['email'], unique=True)
    op.create_table('Patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('clinic_id', sa.Integer(), nullable=True),
    sa.Column('patient_snils', sa.String(length=11), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('sex', sa.String(length=1), nullable=True),
    sa.ForeignKeyConstraint(['clinic_id'], ['Clinics.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Robots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('clinic_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['clinic_id'], ['Clinics.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Robots')
    op.drop_table('Patients')
    op.drop_index(op.f('ix_Users_email'), table_name='Users')
    op.drop_table('Users')
    op.drop_table('Clinics')
    # ### end Alembic commands ###
