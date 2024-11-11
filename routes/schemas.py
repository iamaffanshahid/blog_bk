from pydantic import BaseModel, Field
from typing import List, Optional, Union, Any
from datetime import datetime


# Pydantic model for request and response
class PostCreateSchema(BaseModel):
    title: str
    author: str
    content: str
    created_at: datetime
    # tags: Optional[List[str]] = []

    class Config:
        from_attributes = True
        orm_mode = True


class PostSchema(PostCreateSchema):
    id: int


class ReturnResponseModel(BaseModel):
    data: Union[str, dict, Any, PostSchema, List[PostSchema]]
    message: str
    status: int


class UserSchema(BaseModel):
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

    class Config:
        from_attributes = True
        orm_mode = True


class UserInDB(UserSchema):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class SignUp(BaseModel):
    username: str
    hashed_password: str = Field(alias="password")
    email: str
