from fastapi import FastAPI
from pydantic import BaseModel

class TodoModel(BaseModel):
    id: int | None = None
    item: str | None = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/todo")
async def get_todo_list():
    pass 

@app.post("/todo")
async def create_item(item: TodoModel):
    return {"item": item}