import os

from dotenv import load_dotenv

# APP_ENV picks the settings file: dev (default) -> .env.dev, staging -> .env.staging.
# Real environment variables (e.g. set by the hosting platform) always win,
# because load_dotenv does not override values that are already set.
APP_ENV = os.getenv("APP_ENV", "dev")
load_dotenv(f".env.{APP_ENV}")


class Settings:
    def __init__(self) -> None:
        self.APP_ENV = APP_ENV
        self.DEBUG = APP_ENV == "dev"
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise RuntimeError("DATABASE_URL is not set")
        self.DATABASE_URL = database_url
        self.POOL_SIZE = int(os.getenv("POOL_SIZE", 5))
        self.POOL_TIMEOUT = int(os.getenv("POOL_TIMEOUT", 30))
        self.MAX_OVERFLOW = int(os.getenv("MAX_OVERFLOW", 10))
        self.POOL_RECYCLE = int(os.getenv("POOL_RECYCLE", 300))


settings = Settings()
