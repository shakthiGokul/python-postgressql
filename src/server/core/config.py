import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self) -> None:
        database_url = os.getenv("DATABASE_URL")
        if not database_url:
            raise RuntimeError("DATABASE_URL is not set")
        self.DATABASE_URL = database_url
        self.POOL_SIZE = int(os.getenv("POOL_SIZE", 5))
        self.POOL_TIMEOUT = int(os.getenv("POOL_TIMEOUT", 30))
        self.MAX_OVERFLOW = int(os.getenv("MAX_OVERFLOW", 10))
        self.POOL_RECYCLE = int(os.getenv("POOL_RECYCLE", 300))


settings = Settings()
