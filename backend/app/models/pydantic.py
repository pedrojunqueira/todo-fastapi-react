from pydantic import BaseModel

class TodoPayloadSchema(BaseModel):
    text: str

class TodoUpdatePayloadSchema(BaseModel):
    text: str
    completed: bool

class TodoResponseSchema(BaseModel):
    id: int
    text: str
    completed: bool
