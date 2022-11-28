from pydantic import BaseSettings

class Settings(BaseSettings):
    username: str
    password: str

    class Config:
        env_file = ".env"

settings = Settings()