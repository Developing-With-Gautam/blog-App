from fastapi import FastAPI,Depends,HTTPException,status
from typing import List
from schema import Blog,responseModel,User,User2
from models import Blogs,RegisterUserModel
from database import Base, engine,get_db
from sqlalchemy.orm import Session
from hash import Hash
app= FastAPI()

Base.metadata.create_all(engine)


@app.post('/blog',status_code=status.HTTP_201_CREATED)
def blog_request(request:Blog,db:Session = Depends(get_db)):
    new_data = Blogs(title=request.title , body = request.body)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return new_data
    

@app.get('/blog')
def get_blog(db:Session=Depends(get_db)):

    all_blog= db.query(Blogs).all()
    return all_blog


@app.get('/blog/{id}',response_model=responseModel)
def get_blogWithId(id:int,db:Session=Depends(get_db)):

    new_data = db.query(Blogs).filter(Blogs.id == id).first()
    if new_data :
        return new_data
    raise HTTPException(status_code=500,detail="id not valid")

@app.delete('/blog/{id}')
def delete_blog(id:int,db:Session=Depends(get_db)):
    deleteBlog = db.query(Blogs).filter(Blogs.id == id).first()
    if deleteBlog :
        db.delete(deleteBlog)
        db.commit()
        return deleteBlog
    raise HTTPException(status_code=400,detail="id not found ,please provide valid id ")
    

@app.put('/blog/{id}',status_code= status.HTTP_202_ACCEPTED)
def update(id:int, request:Blog,db:Session=Depends(get_db)):
    checkValid = db.query(Blogs).filter(Blogs.id == id).first()
    # if not checkValid:
    #     return "invalid"
    checkValid.title = request.title
    checkValid.body = request.body

    db.commit()
    return checkValid

@app.post('/register',response_model= User2)
def register_user(request:User,db:Session=Depends(get_db)):
    hash_password = Hash.hash_password(request.password)
    new_user = RegisterUserModel(
        name = request.name, 
        email = request.email,
        password=hash_password
        )
    db.add(new_user)
    db.commit()
    print("new user id1",new_user.id)
    db.refresh(new_user)
    print("new user id2",new_user.id)
    return new_user

@app.get('/user',response_model= [User2])
def get_user(db:Session=Depends(get_db)):

    get_user = db.query(RegisterUserModel).all()
    return get_user
    

    