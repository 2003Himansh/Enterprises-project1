from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    description: str


class OrderCreate(BaseModel):
    product_id: int


class UserCreate(BaseModel):
    username: str
    password: str