from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
class UserOut(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True
class PostCreate(BaseModel):
    title: str
    content: str
class PostOut(BaseModel):
    id: int
    title: str
    content: str
    owner: UserOut

    class Config:
        orm_mode = True