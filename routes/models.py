
from typing import List, Optional
from datetime import datetime
from database import Base
from sqlalchemy import  Column, Integer, String, Text, DateTime, ARRAY, Boolean

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime)

class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    full_name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    disabled = Column(Boolean, default=False)
