from typing import List
from pydantic import BaseModel
from schemas.post import Post


# Esquema Pydantic para los usuarios
class UserBase(BaseModel):
    username: str
    email: str


# Esquema Pydantic para recibir datos de usuario
class UserCreate(UserBase):
    password: str


# Esquema Pydantic para devolver datos de usuario
class User(UserBase):
    id: int
    blog_posts: List[Post] = []

    class Config:
        orm_mode = True
