import decimal
from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class StatisticBase(BaseModel):
    date: date
    views: Optional[int] = None
    clicks: Optional[int] = None
    cost: Optional[decimal.Decimal] = Field(None, max_digits=10, decimal_places=2)


class StatisticCreate(StatisticBase):
    pass


# Properties shared by models stored in DB
class StatisticInDBBase(StatisticBase):
    id: int
    cpc: Optional[decimal.Decimal] = None
    cpm: Optional[decimal.Decimal] = None

    class Config:
        orm_mode = True


# Properties to return to client
class Statistic(StatisticInDBBase):
    pass


# Properties stored in DB
class StatisticInDB(StatisticInDBBase):
    pass


class StatisticList(BaseModel):
    result: list[Statistic]
