"""second migration

Revision ID: c743c433e474
Revises: 34c4e8254573
Create Date: 2023-08-18 14:34:01.400730

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'c743c433e474'
down_revision: Union[str, None] = '34c4e8254573'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
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
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    # ### end Alembic commands ###
