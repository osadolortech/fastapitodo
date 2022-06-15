from bson import ObjectId
from fastapi import APIRouter
from config.database import collections_todo
from models.todo_models import Todo
from schemas.todo_schemas import todo_schemas,todos_schemas


todo_route = APIRouter()

@todo_route.get("/")
async def get_all_todos():
    todo = todos_schemas(collections_todo.find())
    return {"status":"ok", "data": todo}

@todo_route.post("/")
async def post_todo(todo: Todo):
    _id = collections_todo.insert_one(dict(todo))
    todo = todos_schemas(collections_todo.find({"_id": _id.inserted_id}))
    return{"status":"ok", "data": todo}

@todo_route.delete("/{id}")
async def delete_todo(id: str):
    collections_todo.find_one_and_delete({"_id": ObjectId(id) })
    return {"status": "ok", "data": "post has been deleted"}