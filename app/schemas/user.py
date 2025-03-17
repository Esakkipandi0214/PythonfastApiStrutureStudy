from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str  # Add password field

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True
