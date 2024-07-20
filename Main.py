#
# A REST Framework built with FastAPI for testing the framework.
#   We are going to be using JWTs, SQLAlchemy, and Pydantic.
#   This API is created to be a foundation of future project that I create u sing Python,
#   and will contain some boilerplate routes that will be replaced.
#

from fastapi import FastAPI, HTTPException, Depends
import routers.Webhooks
import routers.Auth
import models
from Database import SessionLocal, engine
import logging
from starlette import status
from routers.Auth import db_dependency, get_current_user
from typing import Annotated

# TODO: Find a better way to fix passlib version check error. This will be patched in v1.7.5 whenever its released.
logging.getLogger('passlib').setLevel(logging.ERROR)

# Automatically Create Tables for the Models
models.Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)
app.include_router(routers.Webhooks.router)
app.include_router(routers.Auth.router)

user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Authentication Failed')
    return {"User": user}
