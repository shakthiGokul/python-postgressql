import enum

from sqlalchemy import DateTime, Enum, String, func
from sqlalchemy.orm import Mapped, mapped_column

from server.db.base import Base


class AccountStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    DISABLED = "disabled"


class Auth(Base):
    __tablename__ = "Auth"
    customer_id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(255))
    account_status: Mapped[AccountStatus] = mapped_column(
        Enum(
            AccountStatus,
            name="ck_auth_account_status",  # name of the CHECK constraint in Postgres
            native_enum=False,  # stored as VARCHAR + CHECK constraint: easy to add values later
            length=20,
            # store "active", not "ACTIVE"
            values_callable=lambda e: [member.value for member in e],
            create_constraint=True,
            validate_strings=True,
        ),
        default=AccountStatus.ACTIVE,
        server_default=AccountStatus.ACTIVE.value,
    )
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
