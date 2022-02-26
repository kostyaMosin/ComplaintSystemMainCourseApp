from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str


class BaseComplaint(BaseModel):
    title: str
    description: str
    amount: float
