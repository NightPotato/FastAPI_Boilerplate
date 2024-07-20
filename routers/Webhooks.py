
from fastapi import APIRouter, Request


router = APIRouter(
    prefix='/events',
    tags=['Events']
)


@router.post('/newSub')
async def new_subscriber_event(request: Request):
    """
     External Data provided from the PayPal New Subscriber Webhook
    """
    print(request.json())

    # Do Something with the data, could save parts to the database for automation or use websockets
    # to send it to a Discord bot for alerting.

    return {'message': 'Webhook successfully received.'}