from fastapi import FastAPI
from .models import User
from .crud import create_user_in_db, get_user_from_db

app = FastAPI()

@app.get("/")
def first_page():
    return {"message": "Hello world"}

@app.post("/create")
def create_user(user: User):
    create_user_in_db(user)
    return {
        "id": user.id,
        "name": user.name,
        "message": "User created successfully"
    }

@app.get("/user/{id}")
def get_user(id: int):
    user = get_user_from_db(id)
    if user:
        return {
            "id": user[0],
            "name": user[1],
            "message": f"User {user[0]} fetched successfully"
        }
    else:
        return {"error": "User not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8001, reload=True)