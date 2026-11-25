from typing import Iterator

from sqlalchemy.orm import Session, sessionmaker

from server.db.engine import engine

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
)


def get_session() -> Iterator[Session]:
    with SessionLocal() as session:
        yield session
