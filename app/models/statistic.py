from sqlalchemy import DECIMAL, Column, Date, Integer

from app.db.base_class import Base


class Statistic(Base):
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, nullable=False)
    views = Column(Integer, nullable=True)
    clicks = Column(Integer, nullable=True)
    cost = Column(DECIMAL(10, 2), nullable=True)
    cpc = Column(DECIMAL(10, 2), nullable=True)
    cpm = Column(DECIMAL(10, 2), nullable=True)
