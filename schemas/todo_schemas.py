def todo_schemas(todo) -> dict:
    return{
        "id": str(todo["_id"]),
        "title": todo["title"],
        "completed": todo["completed"]
    }

def todos_schemas(todos) -> list:
    return [todo_schemas(todo) for todo in todos]