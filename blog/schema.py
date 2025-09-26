from fastapi import FastAPI
from pydantic import BaseModel,Field,EmailStr

class Blog(BaseModel):
    title : str
    body: str

class responseModel(BaseModel):
    title:str
    body:str

class User(BaseModel):
    name:str=Field(description="give the name of the user")
    email:EmailStr=Field(description="email of the user")
    password:str=Field(description="give the proper pass")


class User2(BaseModel):
    name:str=Field(description="give the name of the user")
    email:EmailStr=Field(description="email of the user")
    