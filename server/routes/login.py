from fastapi import APIRouter, Depends, status, HTTPException
from server.models.schema import Userinfo
from server.models.model import User
from server.database.database import get_db
from server.utils.utils import (
    verify_password,
    create_access_token,
    refresh_access_token,
)
from sqlalchemy.orm import Session

loginRouter = APIRouter()

"""user login by post method"""


@loginRouter.post("/login")
def login_user(request: Userinfo, db: Session = Depends(get_db)):

    """check whether user name is present in database or not"""
    if not db.query(User).filter(User.user_name == request.user_name).count():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect name or password",
        )

    else:
        user = db.query(User).filter(User.user_name == request.user_name).first()
        user_password = user.password

        """compare login password with hash password"""
        if verify_password(request.password, user_password):
            access_token = create_access_token(user.id)
            refresh_token = refresh_access_token(user.id)

            """returning token"""
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,
            }

        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Incorrect name or password",
            )
