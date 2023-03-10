"""statistic

Revision ID: 0fa5c8bb3db5
Revises:
Create Date: 2022-12-21 16:50:15.700907

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "0fa5c8bb3db5"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "statistic",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("views", sa.Integer(), nullable=True),
        sa.Column("clicks", sa.Integer(), nullable=True),
        sa.Column("cost", sa.DECIMAL(precision=10, scale=2), nullable=True),
        sa.Column("cpc", sa.DECIMAL(precision=10, scale=2), nullable=True),
        sa.Column("cpm", sa.DECIMAL(precision=10, scale=2), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_statistic_id"), "statistic", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_statistic_id"), table_name="statistic")
    op.drop_table("statistic")
    # ### end Alembic commands ###
