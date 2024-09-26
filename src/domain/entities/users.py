from dataclasses import dataclass

from src.domain.entities.base import BaseEntity
from src.domain.values.users import (
    Id,
    Name,
    Email,
)

@dataclass(eq=False)
class UserRequest(BaseEntity):
    user_id: Id

@dataclass(eq=False)
class UserResponse(BaseEntity):
    name: Name
    email: Email
