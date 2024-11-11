from fastapi import FastAPI
import uvicorn
from routes.user import user_router
from routes.oauth import auth_router
from routes.posts import post_router
from base import Base
from database import engine


app = FastAPI()


app.include_router(auth_router, prefix="/api", tags=["auth"])
app.include_router(user_router, prefix="/api", tags=["users"])
app.include_router(post_router, prefix="/api", tags=["post"])


@app.get("/")
async def root():
    return {"message": "API is working"}


def create_tables():
    print("create_tables")
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
