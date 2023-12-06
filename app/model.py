from pydantic import BaseModel
from typing import Optional


class Habit(BaseModel):
    id: Optional[int] = None
    name: str
    start_date: str
    end_date: str
    status: str
