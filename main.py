from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn
app = FastAPI()

@app.get('/')
async def homePage():
    return {'data': {
        "name":"Gautam",
        "age":22
    }
 }

@app.get('/about')
async def about():
    return {"about": {
        "detail":"I am so busy ,frusturate ,blank,everything",
        "solution": " MATA JI SB SAMBHAL LENGI"
    }}
@app.get('/post')
def get_post(limit:int = 10 , published:bool=False, sort_by:Optional[str]=None):
    if sort_by:
        return "sort addedddd"
    if published :
        return {f"this is schedule called {published}"}
    else:
        return {f"this is limit called {limit}"}
    

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]


@app.post('/blog')
def blog(blog:Blog):
    return blog


# if __name__ == "__main__":
#     uvicorn.run(app,host = "127.0.0.1",port=9000)
