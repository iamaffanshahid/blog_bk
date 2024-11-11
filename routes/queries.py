from routes.models import Post
from routes.schemas import PostCreateSchema, PostSchema, SignUp, UserSchema
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException
from routes.models import User
from routes.hash_fuctions import get_password_hash
from sqlalchemy import or_


async def insert_post(post: PostCreateSchema, PostSchema):

    post = Post(**post)
    post.save()


def get_post_by_id(db: Session, item_id: int):
    return db.query(Post).filter(Post.id == item_id).first()


def get_post(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()


def insert_post(db: Session, post: PostCreateSchema):
    post_object = Post(**post.model_dump())
    db.add(post_object)
    db.commit()
    db.refresh(post_object)

    return PostSchema.from_orm(post_object)


def delete_post(db: Session, item_id: int):
    post = get_post_by_id(db, item_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    print("post-------->", post)
    db.delete(post)
    db.commit()
    return item_id


def post_update(db: Session, item_id: int, post: PostCreateSchema):

    post_in_db = db.query(Post).filter(Post.id == item_id).first()
    if post_in_db is None:
        raise HTTPException(status_code=404, detail="Post not found")

    # Update the fields
    post_in_db.title = post.title
    post_in_db.author = post.author
    post_in_db.content = post.content
    post_in_db.created_at = (
        post.created_at
    )  # Assuming you want to update the timestamp as well

    # Commit the changes
    db.commit()
    db.refresh(post_in_db)

    return PostSchema.from_orm(post_in_db)


def insert_user(db: Session, user: SignUp):

    # pasword hashing applied here
    user.hashed_password = get_password_hash(user.hashed_password)

    user_object = User(**user.model_dump())
    db.add(user_object)
    db.commit()
    db.refresh(user_object)

    return UserSchema.from_orm(user_object)


def find_user_by_username_or_email(db: Session, email, username):
    return (
        db.query(Post)
        .filter(or_(User.email == email, User.username == username))
        .first()
    )
