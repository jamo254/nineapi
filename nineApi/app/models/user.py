from tortoise import fields
from tortoise.models import Model


from pydantic import BaseModel
from pydantic_settings import BaseSettings
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)

    class Meta:
        table = "users"
