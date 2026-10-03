from sqlalchemy.orm import Session
from sqlalchemy import select


from app.models.exhibit import Exhibit


def get_exhibits(db: Session):
    return db.scalars(select(Exhibit)).all()