from routes.queries import get_post,post_update,get_post_by_id,delete_post,insert_post
from fastapi import Depends,status
from routes.schemas import PostCreateSchema
from sqlalchemy.orm import Session
from database import get_db
from routes.oauth import oauth2_scheme

from fastapi import APIRouter

post_router = APIRouter()


@post_router.post("/post")
async def create_post( post: PostCreateSchema, db: Session = Depends(get_db),token: str= Depends(oauth2_scheme)):

    print("post", post)

    post_object = insert_post(db=db, post=post)

    content = {
        "data": post_object,
        "message": "Created",
        "status": status.HTTP_201_CREATED
    }
    return content,{"token":token}




@post_router.get("/post")
async def post_get(db: Session = Depends(get_db)):

    post_object = get_post(db=db)

    content = {
        "data": post_object,
        "message": "Ok",
        "status": status.HTTP_200_OK
    }
    return content

@post_router.get("/post/{id}")
async def post_get_by_id(id: int, db: Session = Depends(get_db)):

    post_object = get_post_by_id(db=db, item_id=id)

    content = {
        "data": post_object,
        "message": "Ok",
        "status": status.HTTP_200_OK
    }
    return content

@post_router.delete("/post/{id}")
async def post_delete(id:int, db: Session = Depends(get_db),token:str=Depends(oauth2_scheme)):

    post_id = delete_post(db=db, item_id = id)

    content = {
        "data": post_id,
        "message": "Deleted",
        "status": status.HTTP_200_OK
    }
    return content,{"token":token}

@post_router.put("/post/{id}")
async def update_post(id:int, post:PostCreateSchema, db: Session = Depends(get_db),token:str=Depends(oauth2_scheme)):

    post_id = post_update(db=db, item_id = id, post = post)

    content = {
        "data": post_id,
        "message": "updated",
        "status": status.HTTP_200_OK
    }
    return content,{"token":token}