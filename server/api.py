from fastapi import FastAPI
from server.routes.login import loginRouter
from server.routes.signup import signupRouter

app = FastAPI()

@app.get("/")
def home():
    """simple home page routes

    Returns:
        _type_: _description_
    """
    return {"data": "you are at the home page"}


app.include_router(signupRouter, tags=['signup'])
app.include_router(loginRouter, tags=['login'])
