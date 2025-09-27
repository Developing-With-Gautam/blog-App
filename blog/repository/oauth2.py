from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException
from .jwtToken import verify


oauth2_scheme =  OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token:str = Depends(oauth2_scheme)):
    ceredentials_exception = HTTPException(
        status_code= 401,
        detail="could not validate",
        headers={"WWW-authenticate" : "bearer" },
    )
    return verify(token,ceredentials_exception)




 