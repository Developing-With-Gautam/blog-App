
from jose import JWTError,jwt
from datetime import datetime , timedelta
from schema import Token_Data

SECRET_KEY = "fsdfsdjfhewsrpdihkfjncsdxljkfhncdslkjfhnlcsdf"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 30

def create_access_token(data:dict):
    to_encode = data.copy()
    expire = datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm= ALGORITHM)
    return encode_jwt

def verify(token:str,ceredentials_exception):
    try:
        payload  = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str = payload.get("sub")
        if email is None:
           raise ceredentials_exception
        token_data=Token_Data(email=email)
        return token_data
    except :
        raise ceredentials_exception

    