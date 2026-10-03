from sqlalchemy.orm import Session

from app.models.exhibit import Exhibit


def get_exhibits(db: Session):
    return db.query(Exhibit).all()