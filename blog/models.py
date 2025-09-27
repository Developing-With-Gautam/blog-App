from database import Base,engine
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship


class Blogs(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String,nullable=False)
    body = Column(String,nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    creator = relationship("RegisterUserModel",back_populates="blogs")

class RegisterUserModel(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)
    blogs = relationship("Blogs",back_populates='creator')
