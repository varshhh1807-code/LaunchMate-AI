from sqlalchemy import Column, Integer, String
from database import Base

class ChatHistory(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username= Column(String,unique=True)
    password = Column(String)