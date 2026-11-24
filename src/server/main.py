from sqlalchemy import text

from server.db.engine import engine


def main():
    with engine.connect() as connection:
        version = connection.execute(text("SELECT version()")).scalar_one()
        print(f"Connected to Neon: {version}")


if __name__ == "__main__":
    main()
