from tortoise import fields
from tortoise.models import Model

class Todo(Model):
    id = fields.IntField(pk=True)
    text = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)
    completed = fields.BooleanField(default=False)

    def __str__(self):
        return self.text