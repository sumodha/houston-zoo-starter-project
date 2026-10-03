from sqlalchemy import Column, Integer, String, Text

from app.database import Base


class Exhibit(Base):
    __tablename__ = "exhibits"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    description = Column(Text, nullable=False)