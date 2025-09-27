from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Blogs
from schema import BaseModel,Blog,BlogRelationship

def get_all(db:Session):
   blogs= db.query(Blogs).all()
   return blogs

def create(request:Blog,db:Session):
    new_data = Blogs(title=request.title , body = request.body,user_id=1)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data
    

def delete(id:int,db:Session):
    deleteBlog = db.query(Blogs).filter(Blogs.id == id).first()
    if deleteBlog :
        db.delete(deleteBlog)
        db.commit()
        return f"blog deleted with id {id}"
    raise HTTPException(status_code=400,detail="id not found ,please provide valid id ")


def get_by_id(id:int,db:Session):

    new_data = db.query(Blogs).filter(Blogs.id == id).first()
    if new_data :
        return new_data
    raise HTTPException(status_code=500,detail="id not valid")

def update(id:int,db:Session,request:Blog):
    checkValid = db.query(Blogs).filter(Blogs.id == id).first()
  
    checkValid.title = request.title
    checkValid.body = request.body

    db.commit()
    return {"data update successfully"}