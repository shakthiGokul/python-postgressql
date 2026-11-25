import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from sqlalchemy import inspect, text
from server.db.base import Base
from server.db.engine import engine
from server.models.customers_model import Customers  # noqa: F401  (registers the customers table with Base)
from server.api.v1.customers_api import router as Customers_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(engine)
    yield
    engine.dispose()

app = FastAPI(title="CRM" , lifespan= lifespan)
app.include_router(Customers_router)

@app.get("/health")
def health():
    return {"status": "ok"}

def main():
    uvicorn.run("server.main:app" , reload= True)
   


if __name__ == "__main__":
    main()
