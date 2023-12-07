from fastapi import FastAPI

from app.model import Habit

app = FastAPI()

habits = []



@app.get("/api/hello")
async def hello_world(name: str):
    return {"message": f"Hello {name}!"}


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


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
