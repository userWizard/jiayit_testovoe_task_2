import httpx

from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter

from src.application.api.shemas import ErrorSchema
from src.application.api.users.shemas import UserRequestSchema, UserResponseSchema
from src.common.temps import EXTERNAL_API_URL
from src.domain.exceptions.base import ApplicationException

router = APIRouter(tags=['User'])

@router.post(
    '/user',
    status_code=status.HTTP_201_CREATED,
    description='',
    response={
        status.HTTP_201_CREATED: {'model': UserResponseSchema},
        status.HTTP_400_BAD_REQUEST: {'model': ErrorSchema},
    },
)
async def user(schema: UserRequestSchema):
    '''Получение пользователя.'''
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{EXTERNAL_API_URL}/{schema.user_id}")
        try: 
            user_data = response.json()
        except ApplicationException as exception:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'error': exception.message})
        
    return UserResponseSchema.from_entity(user_data)