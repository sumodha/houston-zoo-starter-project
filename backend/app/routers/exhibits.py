from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.exhibit import ExhibitResponse
from app.services.exhibit_service import get_exhibits


router = APIRouter(
    prefix="/exhibits",
    tags=["exhibits"]
)


@router.get("/", response_model=list[ExhibitResponse])
def read_exhibits(db: Session = Depends(get_db)):
    return get_exhibits(db)