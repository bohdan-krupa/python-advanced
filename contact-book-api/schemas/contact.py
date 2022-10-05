import re
from typing import Optional
from datetime import datetime
from pydantic import EmailStr, constr
from schemas.camel_model import CamelModel

PhoneStr = constr(regex="^[0-9]{10,12}$")


class ContactIn(CamelModel):
    first_name: str
    last_name: Optional[str]
    phone: PhoneStr
    email: Optional[EmailStr]

    class Config:
        orm_mode = True


class ContactOut(ContactIn):
    id: int
    created_at: datetime
