"""empty message

Revision ID: 661597ed555d
Revises: 
Create Date: 2020-08-01 23:40:06.778759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '661597ed555d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('description', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('mobile_no', sa.String(length=12), nullable=False),
    sa.Column('password', sa.String(length=15), nullable=False),
    sa.Column('role', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('mobile_no')
    )
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=70), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('country', sa.String(length=70), nullable=True),
    sa.Column('state_UT', sa.String(length=70), nullable=True),
    sa.Column('district', sa.String(length=70), nullable=True),
    sa.Column('city_village', sa.String(length=70), nullable=True),
    sa.Column('locality', sa.String(length=70), nullable=True),
    sa.Column('house_no', sa.String(length=70), nullable=True),
    sa.Column('pincode', sa.String(length=10), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('pay_method', sa.String(length=50), nullable=True),
    sa.Column('pay_amount', sa.Float(), nullable=True),
    sa.Column('pay_reference', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('pay_reference')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prod_code', sa.String(length=100), nullable=True),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('prod_code')
    )
    op.create_table('tree',
    sa.Column('descendant', sa.Integer(), nullable=False),
    sa.Column('ancestor', sa.Integer(), nullable=False),
    sa.Column('length', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['ancestor'], ['categories.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['descendant'], ['categories.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('descendant', 'ancestor')
    )
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.CheckConstraint(u'quantity > 0'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=500), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('prod_id', sa.Integer(), nullable=True),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('downvotes', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['prod_id'], ['products.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('order_date_time', sa.DateTime(), nullable=False),
    sa.Column('order_status', sa.String(length=70), nullable=True),
    sa.Column('order_value', sa.Float(), nullable=True),
    sa.Column('payment_id', sa.Integer(), nullable=True),
    sa.Column('address_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.ForeignKeyConstraint(['payment_id'], ['payments.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('payment_id')
    )
    op.create_table('product_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('products_meta',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('image1_url', sa.String(length=500), nullable=True),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('inventory_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wishlist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order_products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Float(), nullable=True),
    sa.CheckConstraint(u'quantity > 0'),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_products')
    op.drop_table('wishlist')
    op.drop_table('products_meta')
    op.drop_table('product_categories')
    op.drop_table('orders')
    op.drop_table('comments')
    op.drop_table('cart')
    op.drop_table('tree')
    op.drop_table('products')
    op.drop_table('payments')
    op.drop_table('address')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###
