
from fastapi import APIRouter,Depends

from schema import User,User2,User3,userLogin
from sqlalchemy.orm import Session
from database import get_db
from repository import users

router = APIRouter(
     prefix='/user',
     tags=['User']
)

@router.post('/',response_model= User2)
def register_user(request:User,db:Session=Depends(get_db)):
    return users.create(request,db)

@router.get('/')
def get_user(db:Session=Depends(get_db)):
    return users.get_user(db)


@router.get('/{id}',response_model=User3)
def get_user_with_id(id:int,db:Session=Depends(get_db)):
    return users.get_userId(id,db)



    
