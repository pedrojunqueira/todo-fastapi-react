import logging

from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import (
    TodoPayloadSchema,
    TodoResponseSchema,
    TodoUpdatePayloadSchema,
)

router = APIRouter()

log = logging.getLogger("uvicorn")


@router.post("/", response_model=TodoResponseSchema, status_code=201)
async def create_todo(payload: TodoPayloadSchema):
    todo_id = await crud.create_todo(payload)
    todo = await crud.get_todo(todo_id)
    
    return TodoResponseSchema(
        id=todo_id,
        text=todo.text,
        completed=todo.completed
    )

@router.get("/", response_model=list[TodoResponseSchema], status_code=200)
async def get_all_todos():
    todos = await crud.get_all_todos()
    return [
        TodoResponseSchema(
            id = t.id,
            text = t.text,
            completed=t.completed

        ) for t in todos
    ]

@router.get("/{id}/", response_model=TodoResponseSchema)
async def get_todo(id:int):
    todo = await crud.get_todo(id)
    if not todo:
        raise HTTPException(status_code=400, detail="Todo not found")
    return TodoResponseSchema(
        id= todo.id,
        text= todo.text,
        completed=todo.completed
    )

@router.put("/{id}/", response_model=TodoResponseSchema)
async def update_todo(id: int, payload: TodoUpdatePayloadSchema):
    todo = await crud.update_todo(id, str(payload.text), payload.completed)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return TodoResponseSchema(
        id=todo.id,
        text=str(todo.text),
        completed= todo.completed
    )

@router.delete("/{id}/")
async def delete_todo(id: int):
    deleted = await crud.delete_todo(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"id": id, "deleted": True}