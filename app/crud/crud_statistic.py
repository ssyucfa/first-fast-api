from datetime import date

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.statistic import Statistic
from app.schemas.statistic import StatisticCreate


class CRUDStatistic(CRUDBase[Statistic, StatisticCreate, ...]):
    def get_all(self, db: Session) -> list[Statistic]:
        return db.query(self.model).all()

    def create(self, db: Session, *, obj_in: StatisticCreate) -> Statistic:
        obj_in_data = obj_in.dict()

        if obj_in.cost and obj_in.clicks:
            obj_in_data["cpc"] = round(obj_in.cost / obj_in.clicks, 2)

        if obj_in.cost and obj_in.views:
            obj_in_data["cpm"] = round(obj_in.cost / obj_in.views * 1000, 2)

        db_obj = self.model(**obj_in_data)  # type: ignore

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)

        return db_obj

    def remove_all(self, db: Session) -> None:
        db.query(self.model).delete()
        db.commit()

    def filter(
        self, db: Session, *, since: date, until: date, order_by: str
    ) -> list[Statistic]:
        return (
            db.query(self.model)
            .filter(self.model.date >= since, self.model.date <= until)
            .order_by(order_by)
            .all()
        )


statistic = CRUDStatistic(Statistic)
