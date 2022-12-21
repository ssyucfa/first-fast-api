from datetime import date, timedelta
from typing import Literal

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app import crud
from app.api import deps
from app.schemas.statistic import Statistic, StatisticCreate, StatisticList

router = APIRouter()


@router.get("/", status_code=200, response_model=StatisticList)
def get_statistics(
    *,
    since: date = Query(..., example=date.today()),
    until: date = Query(..., example=date.today() + timedelta(days=1)),
    order_by: Literal["id", "date", "views", "clicks", "cost", "cpc", "cpm"] = Query(
        "date"
    ),
    db: Session = Depends(deps.get_db)
) -> dict:
    """
    All statistics.
    """
    statistics = crud.statistic.filter(
        db=db, since=since, until=until, order_by=order_by
    )

    return {"result": statistics}


@router.post("/", status_code=201, response_model=Statistic)
def create_statistic(
    *, statistic_in: StatisticCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new statistic.
    """
    statistic = crud.statistic.create(db=db, obj_in=statistic_in)

    return statistic


@router.delete("/", status_code=204)
def delete_statistics(*, db: Session = Depends(deps.get_db)) -> None:
    """
    delete all statistics.
    """
    crud.statistic.remove_all(db=db)
