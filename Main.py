#
# A REST Framework built with FastAPI for testing the framework.
#   We are going to be using JWTs, SQLAlchemy, and Pydantic.
#   This API is created to be a foundation of future project that I create u sing Python,
#   and will contain some boilerplate routes that will be replaced.
#

from typing import Union
from fastapi import FastAPI, Request
import routers.Webhooks
import routers.Auth


app = FastAPI()
app.include_router(routers.Webhooks.router)
app.include_router(routers.Auth.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
