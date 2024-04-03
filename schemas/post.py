from pydantic import BaseModel


# Esquema Pydantic para las publicaciones de blog
class PostBase(BaseModel):
    title: str
    content: str


# Esquema Pydantic para recibir datos de publicación de blog
class PostCreate(PostBase):
    pass


# Esquema Pydantic para devolver datos de una publicación de blog
class Post(PostBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True
