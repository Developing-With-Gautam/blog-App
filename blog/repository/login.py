
from schema import userLogin
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import RegisterUserModel
from .jwtToken import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from hash import Hash

def login(request:OAuth2PasswordRequestForm,db:Session):
   UserL= db.query(RegisterUserModel).filter(RegisterUserModel.email == request.username).first()

   if not UserL:
      raise HTTPException(status_code=401,detail="email not valid")
   if not Hash.verify_password(request.password, UserL.password):
      raise HTTPException(status_code=401, detail="password is incorrect")
   
   access_token = create_access_token( data = {
      "sub":UserL.email
   })
   return { "access_token" :access_token , "token-type":"bearer" }
  

   

