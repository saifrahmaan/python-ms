"""third migration

Revision ID: 968e2853f041
Revises: c743c433e474
Create Date: 2023-08-18 15:17:18.856100

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '968e2853f041'
down_revision: Union[str, None] = 'c743c433e474'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sku', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('short_details', sa.Text(), nullable=True),
    sa.Column('details', sa.Text(), nullable=True),
    sa.Column('stock', sa.BigInteger(), nullable=True),
    sa.Column('price', sa.BigInteger(), nullable=True),
    sa.Column('discount', sa.BigInteger(), nullable=True),
    sa.Column('lat_long', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('delivery_type', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.Column('stock_check_number', sa.String(length=255), nullable=True),
    sa.Column('thumbnail_image', sa.String(length=255), nullable=True),
    sa.Column('seller_id', sa.BigInteger(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=True),
    sa.Column('verification_status', sa.String(length=255), nullable=True),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('approved_by', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Products')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Products',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('sku', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('short_details', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('details', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('stock', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('price', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('discount', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('lat_long', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('delivery_type', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('stock_check_number', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('thumbnail_image', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('seller_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('rating', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('verified', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('verification_status', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('comment', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('approved_by', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='product_pkey')
    )
    op.drop_table('products')
    # ### end Alembic commands ###
