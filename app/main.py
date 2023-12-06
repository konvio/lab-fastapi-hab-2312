from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Habit(BaseModel):
    id: Optional[int] = None
    name: str
    start_date: str
    end_date: str
    status: str


app = FastAPI()

habits = []


@app.post("/habits/")
async def create_habit(habit: Habit):
    habit.id = len(habits) + 1
    habits.append(habit.model_dump())
    return habit.model_dump()


@app.get("/habits/")
async def get_habits():
    return habits


@app.get("/habits/{habit_id}")
async def get_habit(habit_id: int):
    for habit in habits:
        if habit["id"] == habit_id:
            return habit
    return {"error": "Habit not found"}


@app.put("/habits/{habit_id}")
async def update_habit(habit_id: int, habit: Habit):
    for index, existing_habit in enumerate(habits):
        if existing_habit["id"] == habit_id:
            habits[index] = habit.dict()
            habits[index]["id"] = habit_id
            return habits[index]
    return {"error": "Habit not found"}


@app.delete("/habits/{habit_id}")
async def delete_habit(habit_id: int):
    for index, existing_habit in enumerate(habits):
        if existing_habit["id"] == habit_id:
            habits.pop(index)
            return {"message": "Habit deleted"}
    return {"error": "Habit not found"}
