# For Data Validations
from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, constr

print("hello")
class UserAdd(BaseModel):
    name: str
    surname: str
    email: EmailStr
    password: str
    passport_id: str


class UserOut(BaseModel):
    name: str
    email: EmailStr


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UpdateSettings(BaseModel):
    language: str
    background_color: str
    font_size: int


class PasswordReset(BaseModel):
    new_password: str
    mail: str
    confirm_password: str


class BookAdd(BaseModel):
    title: str
    publisher_id: int
    author_id: int
    quantity: int


class BookOut(BaseModel):
    title: str
    publisher_name: str
    author_name: str


#stugel ete ayd grqic ka qanaky avelacnel ete che taza girq avelacnel


class AuthorAdd(BaseModel):
    name: constr(max_length=100)
    surname: constr(max_length=100)
    born: Optional[date]


class AuthorOut(AuthorAdd):
    id: int


class Publisher(BaseModel):
    name: str
    address: Optional[str]
    email: EmailStr


class PublisherOut(BaseModel):
    pass








