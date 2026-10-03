from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.exhibit import Exhibit
from app.routers import exhibits
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


Base.metadata.create_all(bind=engine)

seed_database()


app = FastAPI(
    title="Mini Zoo API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(exhibits.router)


@app.get("/health")
def health():
    return {"status": "ok"}