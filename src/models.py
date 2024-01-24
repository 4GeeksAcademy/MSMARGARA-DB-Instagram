import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Boolean, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=True)
    first_name = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    contact = Column(String(10), nullable=False)
    birth_date_time = Column(DateTime, nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(8), nullable=False)
    profile_pic = Column(String(250), nullable=True)
    bio = Column(String(250), nullable=True)
    gender_id = Column(Integer, ForeignKey('gender.id'), nullable= True)
    account_status = Column(Boolean, nullable= False)
    link = Column(String(250), nullable=True)
    account_type = Column(Integer, ForeignKey('account_type.id'), nullable=False)
    avatar = Column(String(250), nullable=True)

class Gender(Base):
    __tablename__ = 'gender'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)

class AccountType(Base):
    __tablename__='account_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    
class AcceptanceStatus(Enum):
    ACEPTADO = "aceptado"
    RECHAZADO = "rechazado"
    PENDIENTE = "pendiente"

class Followers(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    follower_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    accepted = Column(Enum(AcceptanceStatus), nullable=False)

class Post(Base):
    __tablename__='post'
    id= Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    description = Column(String(250), nullable=True)

class Media(Base):
    __tablename__='media'
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(Enum('image', 'video', name='media_types'), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

class Comments(Base):
    __tablename__='comments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column (Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    content = Column(String(250), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

class Likes(Base):
    __tablename__='likes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
