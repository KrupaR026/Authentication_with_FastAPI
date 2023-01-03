from pydantic import BaseModel

"""schema for your signup"""


class Usersauth(BaseModel):
    user_name: str
    email: str
    password: str

    class config:
        orm_mode = True


"""schema for user signup response"""


class Displayuser(BaseModel):
    id: int
    user_name: str
    email: str

    class Config:
        orm_mode = True


"""schema for user logging"""


class Userinfo(BaseModel):
    user_name: str
    password: str

    class Config:
        orm_mode = True
