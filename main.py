from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def homePage():
    return {'data': {
        "name":"Gautam",
        "age":34
    }
 }

@app.get('/about')
async def about():
    return {"about": {
        "detail":"I am so busy ,frusturate ,blank,everything",
        "solution": " MATA JI SB SAMBHAL LENGI"
    }}

