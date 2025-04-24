from fastapi import FastAPI
from pydantic import BaseModel
import pymysql
import uvicorn

connection= pymysql.connect(
     host ='localhost',
     user = 'root',
     password = '123',
     database = 'User_Data'
)
cursor = connection.cursor();

class User(BaseModel):
    id: int
    name: str

app = FastAPI()
@app.get("/")
def first_page():
    return{"message": "Hello world"}

@app.post("/create")
def create_user(id,name):
    cursor.execute('INSERT INTO User_Data.user(id,name) values(%s,%s)',(id,name)) 
    connection.commit()
    return{"id": {id} , "name" : {name} , "message": "created user"}





if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)