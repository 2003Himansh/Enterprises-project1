from pydantic import BaseSettings


class Settings(BaseSettings):

    DEBUG: bool = True
    HOST: str = "127.0.0.1"
    PORT: int = 8000

    SECRET_KEY: str = "mysecretkey"

    ALLOWED_ORIGINS: list = ["*"]
    ALLOWED_HOSTS: list = ["*"]

    class Config:
        env_file = ".env"


settings = Settings()