"""add foreign key to posts table

Revision ID: dca672d9bc26
Revises: 54cd2de04ef8
Create Date: 2022-10-31 12:15:01.579029

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dca672d9bc26'
down_revision = '54cd2de04ef8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_user_fk', source_table="posts", referent_table="users",
    local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_user_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
