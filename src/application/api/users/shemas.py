from pydantic import BaseModel

from src.domain.entities.users import UserResponse

class UserRequestSchema(BaseModel):
    user_id: int


class UserResponseSchema(BaseModel):
    name: str
    email: str
    
    @classmethod
    def from_entity(cls, entity: UserResponse) -> 'UserResponseSchema':
        return UserResponseSchema(
            name=entity.name,
            email=entity.email
        )