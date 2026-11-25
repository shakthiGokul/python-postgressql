from pydantic import BaseModel , EmailStr, Field, ConfigDict
from datetime import datetime

class CreateCustomer(BaseModel):
    first_name: str = Field(min_length= 1 , max_length = 100)
    last_name : str = Field(min_length=1, max_length= 100)
    email_id: EmailStr
    mobile_number: str | None = Field (default= None , max_length=20)

# Full replacement (PUT): clients always send the complete details,
# so the rules are the same as CreateCustomer.
class UpdateCustomer(CreateCustomer):
    pass

class CustomerOut(BaseModel):
    model_config = ConfigDict(from_attributes= True)
    customer_id: int
    first_name: str 
    last_name : str
    email_id: EmailStr
    mobile_number: str | None
    created_at: datetime
    updated_at: datetime