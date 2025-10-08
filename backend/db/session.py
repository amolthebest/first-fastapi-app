from email.generator import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# from core.config import settings


POSTGRES_USER="postgres"
POSTGRES_PASSWORD="root"
POSTGRES_SERVER="localhost"
POSTGRES_PORT=5432
POSTGRES_DB="fast-api-demo"
# SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL
# print("Database URL is ",SQLALCHEMY_DATABASE_URL)
# engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine = create_engine(f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}")


SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()