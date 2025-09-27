from fastapi import APIRouter,Depends
from schema import userLogin
from database import get_db
from sqlalchemy.orm import Session
from repository import login
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter(
     tags=['Authenticaiton']
)


@router.post('/login')
def user_login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    print("user")
    return login.login(request,db)




