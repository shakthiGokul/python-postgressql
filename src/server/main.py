from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from server.api.v1.customers_api import router as Customers_router
from server.db.engine import engine
from server.models.customers_model import Customers  # noqa: F401  (registers the customers table with Base)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Tables are managed by Alembic now, so nothing to create on startup.
    yield
    # Shutdown: close every pooled connection to Neon cleanly.
    engine.dispose()


app = FastAPI(title="CRM", lifespan=lifespan)
app.include_router(Customers_router)

@app.get("/health")
def health():
    return {"status": "ok"}

def main():
    uvicorn.run("server.main:app" , reload= True)
   


if __name__ == "__main__":
    main()
