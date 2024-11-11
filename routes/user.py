
from fastapi import Depends
from routes.oauth import get_current_active_user
from routes.schemas import UserSchema

from fastapi import APIRouter

user_router = APIRouter()


@user_router.get("/users/me/", response_model=UserSchema)
async def read_users_me(current_user: UserSchema = Depends(get_current_active_user)):
    return current_user



@user_router.get("/users/me/items/")
async def read_own_items(current_user: UserSchema = Depends(get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]

