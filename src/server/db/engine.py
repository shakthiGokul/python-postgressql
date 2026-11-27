from sqlalchemy import create_engine

from server.core.config import settings

engine = create_engine(
    settings.DATABASE_URL, 
    pool_size= settings.POOL_SIZE,
    pool_timeout= settings.POOL_TIMEOUT,
    max_overflow= settings.MAX_OVERFLOW ,
    pool_pre_ping= True,
    pool_recycle= settings.POOL_RECYCLE
)