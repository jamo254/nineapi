# nineApi/config/settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "nineApi"
    debug: bool = True

    class Config:
        env_file = ".env"  # You can store environment variables in a .env file.

settings = Settings()
