from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

tasks = ["Дело 1", "Дело 2"]


@app.get("/tasks")
async def get_tasks():
    return {"tasks": tasks}