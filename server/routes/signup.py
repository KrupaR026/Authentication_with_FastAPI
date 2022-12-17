from fastapi import APIRouter, Depends
from server.models.schema import  UserAuth, UserOut
from server.database.database import SessionLocal
from server.utils.utils import get_hashed_password
from uuid import uuid4
from sqlalchemy.orm import session
from server.database.database import get_db
from server.models.model import User

signupRouter = APIRouter()
# db = SessionLocal()

# @signupRouter.post('/signup', summary="Create new user", response_model=UserOut)
# def create_user(data: UserAuth):
#     # querying database to check if user already exist
#     user = db.get(data.email, None)
#     if user is not None:
#             raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="User with this email already exist"
#         )
#     user = {
#         'email': data.email,
#         'password': get_hashed_password(data.password),
#         'id': str(uuid4())
#     }
#     db[data.email] = user    # saving user to database
#     return user

@signupRouter.post("/user_signup", response_model=UserOut)
def signupp(resquest: UserAuth, db: session=Depends(get_db)):
    # convert plain password with hash password
    newuser = User(user_name=resquest.user_name, email = resquest.email, password=get_hashed_password(resquest.password))
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser