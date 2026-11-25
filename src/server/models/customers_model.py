from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from server.db.base import Base


class Customers(Base):
    __tablename__ = "customers"
    customer_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email_id: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    mobile_number: Mapped[str | None] = mapped_column(String(20))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at : Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
        )

    def __repr__(self) -> str:
        return f"User(customer_id={self.customer_id}, email_id={self.email_id!r})"
