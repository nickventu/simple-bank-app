from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    password: str
    email: str

class UserResponse(BaseModel):
    userId: int
    name: str
    email: str
