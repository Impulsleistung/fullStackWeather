from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.utils.simple import execute_something
import asyncio

app = FastAPI()


async def periodic_task():
    while True:
        execute_something()  # Call your function
        await asyncio.sleep(600)  # Wait for 10 minutes (600 seconds)


asyncio.create_task(periodic_task())  # Start the periodic task

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/")
async def get_plot(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
