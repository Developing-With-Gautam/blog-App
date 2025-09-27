from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from schema import BaseModel,Blog,BlogRelationship
from repository import blog
from models import Blogs
from database import get_db
from repository import oauth2
router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

@router.get('/')
def get_all_blog(db:Session=Depends(get_db),current_user:Blog = Depends(oauth2.get_current_user)):
    return blog.get_all(db)


@router.post('/',status_code=status.HTTP_201_CREATED)
def add_blog(request:Blog,db:Session = Depends(get_db),current_user:Blog = Depends(oauth2.get_current_user)):
    return blog.create(request,db)
    

@router.get('/{id}',response_model=BlogRelationship)
def get_blog_with_id(id:int,db:Session=Depends(get_db),current_user:Blog = Depends(oauth2.get_current_user)):
    return blog.get_by_id(id,db)
   

@router.delete('/{id}')
def delete_blog(id:int,db:Session=Depends(get_db),current_user:Blog = Depends(oauth2.get_current_user)):
    return blog.delete(id,db)
   

@router.put('/{id}',status_code= status.HTTP_202_ACCEPTED)
def update_blog(id:int, request:Blog,db:Session=Depends(get_db),current_user:Blog = Depends(oauth2.get_current_user)):
    return blog.update(id,request,db)