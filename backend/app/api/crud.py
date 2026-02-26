from app.models.tortoise import Todo
from app.models.pydantic import TodoPayloadSchema

async def create_todo(payload: TodoPayloadSchema):
    todo = await Todo.create(text=str(payload.text))
    return todo.id

async def get_todo(id: int):
    todo = await Todo.filter(id=id).first()
    return todo

async def get_all_todos():
    return await Todo.all()

async def delete_todo(id: int):
    return await Todo.filter(id=id).delete() > 0

async def update_todo(id: int, text:str, completed:bool):
    todo_object = await Todo.filter(id=id).first()
    if todo_object:
        todo_object.text = text
        todo_object.completed = completed
        await todo_object.save()
    return todo_object


