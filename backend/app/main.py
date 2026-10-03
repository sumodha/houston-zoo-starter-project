from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.exhibit import Exhibit
from app.routers import exhibits
from app.database import SessionLocal
from app.seeds import seed_database


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
