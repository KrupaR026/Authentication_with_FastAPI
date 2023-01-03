from fastapi import APIRouter, Depends, Request
from server.database.database import get_db
from server.models.schema import Usersauth, Displayuser
from server.models.model import User
from sqlalchemy.orm import Session
from server.utils.utils import password_hash, JWTBearer, decodeJWT


signupRouter = APIRouter()


"""secure router for total users"""


@signupRouter.get("/alluser", dependencies=[Depends(JWTBearer())])
def alluser(request: Request, db: Session = Depends(get_db)):

    access_token = request.headers["Authorization"][7:]
    decoded = decodeJWT(access_token)
    print(decoded)
    db_users = db.query(User).all()

    return db_users


"""user signup by post method"""


@signupRouter.post("/user_signup", response_model=Displayuser)
def signupp(request: Usersauth, db: Session = Depends(get_db)):

    """convert plain password to hash password"""
    newuser = User(
        user_name=request.user_name,
        email=request.email,
        password=password_hash(request.password),
    )
    db.add(newuser)
    db.commit()
    db.refresh(newuser)

    return newuser
