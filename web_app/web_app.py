import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import requests

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    tasks_responce = requests.get("http://127.0.0.1:5001/tasks").json()
    print(tasks_responce)
    return templates.TemplateResponse("index.html", {"request": request, "tasks": tasks_responce["tasks"]})

