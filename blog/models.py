from database import Base,engine
from sqlalchemy import Column,Integer,String


class Blogs(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String,nullable=False)
    body = Column(String,nullable=False)

class RegisterUserModel(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)