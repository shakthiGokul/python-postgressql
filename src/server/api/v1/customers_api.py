from typing import Annotated

from fastapi import APIRouter , Depends , HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from server.db.session import get_session
from server.models.customers_model import Customers
from server.schemas.customers_schema import CreateCustomer , UpdateCustomer , CustomerOut

router = APIRouter(prefix='/customers' , tags=["customers"])

SessionDep = Annotated[Session , Depends(get_session)]

def get_customer_or_404(session: Session, customer_id: int) -> Customers:
    customer = session.get(Customers , customer_id)
    if customer is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND , "customer not found")
    return customer

def commit_or_409(session: Session) -> None:
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT , "email already exist")  

@router.post("/create" , response_model= CustomerOut , status_code=status.HTTP_201_CREATED) 
def create_customer(data: CreateCustomer , session: SessionDep):
    customer = Customers(**data.model_dump()) 
    session.add(customer)
    commit_or_409(session)
    session.refresh(customer)
    return customer     

@router.get("" , response_model=list[CustomerOut], status_code= status.HTTP_200_OK)
def get_customers(session: SessionDep, skip: int = 0, limit: int = 50):
    query= select(Customers).order_by(Customers.customer_id).offset(skip).limit(limit)
    return session.scalars(query).all()
    