from sqlalchemy import inspect, text

from server.db.base import Base
from server.db.engine import engine
from server.models.customers_model import Customers  # noqa: F401  (registers the customers table with Base)


def main():
    with engine.connect() as connection:
        version = connection.execute(text("SELECT version()")).scalar_one()
        print(f"Connected to Neon: {version}")

    Base.metadata.create_all(engine)
    print(f"Tables in Neon: {inspect(engine).get_table_names()}")


if __name__ == "__main__":
    main()
