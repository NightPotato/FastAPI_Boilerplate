#
# REST API authentication using OAuth2 or Basic Authentication
#

from fastapi import APIRouter, Request, Response


router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)


@router.post('/login')
async def process_login():
    pass

