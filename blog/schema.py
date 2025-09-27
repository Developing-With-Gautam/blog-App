from fastapi import FastAPI
from pydantic import BaseModel,Field,EmailStr
from typing import List,Optional



class User(BaseModel):
    name:str=Field(description="give the name of the user")
    email:EmailStr=Field(description="email of the user")
    password:str=Field(description="give the proper pass")
    class Config:
        orm_mode = True
    


class User2(BaseModel):
    name:str=Field(description="give the name of the user")
    email:EmailStr=Field(description="email of the user")
    class Config:
        orm_mode = True


class Blog(BaseModel):
    title : str
    body: str
    class Config:
        orm_mode = True

class BlogRelationship(BaseModel):
    title : str
    body: str
    creator:User2
    class Config:
        orm_mode = True


class responseModel(BaseModel):
    title:str
    body:str

    class Config:
        orm_mode = True


class User3(BaseModel):
    name:str=Field(description="give the name of the user")
    email:EmailStr=Field(description="email of the user")
    blogs: List[Blog]
    class Config:
        orm_mode = True


class userLogin(BaseModel):
    email:EmailStr
    password:str

    class Config:
        orm_mode = True

class Toekn(BaseModel):
    access_toke:str
    token_type :str

class Token_Data(BaseModel):
    email:Optional[str] =None