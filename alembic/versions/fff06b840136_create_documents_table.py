"""Create documents table

Revision ID: fff06b840136
Revises: c069b2fcfc7e
Create Date: 2024-11-04 16:09:15.810141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fff06b840136'
down_revision: Union[str, None] = 'c069b2fcfc7e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('documents', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('documents', 'content',
               existing_type=sa.TEXT(),
               type_=sa.String(),
               existing_nullable=True)
    op.create_index(op.f('ix_documents_id'), 'documents', ['id'], unique=False)
    op.create_index(op.f('ix_documents_title'), 'documents', ['title'], unique=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.drop_constraint('users_username_key', 'users', type_='unique')
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('users', 'username',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.drop_index(op.f('ix_documents_title'), table_name='documents')
    op.drop_index(op.f('ix_documents_id'), table_name='documents')
    op.alter_column('documents', 'content',
               existing_type=sa.String(),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.alter_column('documents', 'title',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###