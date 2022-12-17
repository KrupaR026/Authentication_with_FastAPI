from pydantic import BaseModel

class UserAuth(BaseModel):
    user_name: str
    email: str
    password: str

    class Config:
        orm_mode = True

class UserOut(BaseModel):
    user_name: str
    email: str

    class Config:
        orm_mode = True

class TokenSchema(BaseModel):
    access_token: str
    token_type: str

    class Config:
        orm_mode = True
