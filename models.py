from pydantic import BaseModel, EmailStr
from typing import Optional

class Employee(BaseModel):
    id: Optional[int] = None
    name: str
    team: str
    role: str
    email: EmailStr

