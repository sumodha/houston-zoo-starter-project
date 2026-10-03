
from app.models.exhibit import Exhibit
from app.database import SessionLocal

def seed_database():
    db = SessionLocal()

    try:
        if db.query(Exhibit).count() == 0:
            exhibits = [
                Exhibit(
                    name="African Forest",
                    location="North Side",
                    description="Explore wildlife from the forests of Africa."
                ),
                Exhibit(
                    name="Galápagos Islands",
                    location="Central Zoo",
                    description="Discover wildlife inspired by the Galápagos Islands."
                ),
                Exhibit(
                    name="Pantanal",
                    location="South Side",
                    description="Explore animals from the world's largest tropical wetland."
                ),
            ]

            db.add_all(exhibits)
            db.commit()

    finally:
        db.close()
