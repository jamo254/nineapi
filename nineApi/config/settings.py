# nineApi/config/settings.py
from pydantic_settings import BaseSettings

# Defining  database setting
class Settings(BaseSettings):
    app_name: str = "nineApi"
    debug: bool = True
    database_url: str = "sqlite://db.sqlite3"  # Use your desired database URL

    class Config:
        env_file = ".env"

settings = Settings()
