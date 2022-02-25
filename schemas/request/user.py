from schemas.base import BaseUser


class UserRegisterIn(BaseUser):
    password: str
    phone: str
    first_name: str
    last_name: str
    iban: str


class UserLoginIn(BaseUser):
    password: str
