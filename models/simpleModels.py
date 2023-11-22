from typing import Union, Annotated
from pydantic import BaseModel, Field


class User(BaseModel):
    name: Union[str, None] = None
    id: Annotated[int, Field(ge=1)]


class UserBD(User):
    password: Annotated[Union[str, None], Field(min_length=6, max_length=50)] = None
