import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path(".")/".env"
load_dotenv(dotenv_path=env_path)



class Settings:

    PROJECT_NAME : str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "root")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)  # default postgres port is 5432
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "fast-api-demo")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"


settings = Settings()

# print(settings.POSTGRES_USER, settings.POSTGRES_PASSWORD, settings.POSTGRES_SERVER,
#       settings.POSTGRES_PORT, settings.POSTGRES_DB)