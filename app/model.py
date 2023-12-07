from pydantic import BaseModel


class Habit(BaseModel):
    id: str
    name: str
    description: str

