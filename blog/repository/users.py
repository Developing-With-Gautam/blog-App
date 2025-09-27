from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import RegisterUserModel
from schema import User,User2,User3,userLogin
from hash import Hash



def create(request:User,db:Session):
    hash_password = Hash.hash_password(request.password)
    new_user = RegisterUserModel(
        name = request.name, 
        email = request.email,
        password=hash_password
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db:Session):
    get_user = db.query(RegisterUserModel).all()
    return get_user

def get_userId(id:int,db:Session):
    get_user = db.query(RegisterUserModel).filter(id == RegisterUserModel.id).first()
    if get_user:
        return get_user
    raise HTTPException (status_code=401,detail="user with this id not find")


    

