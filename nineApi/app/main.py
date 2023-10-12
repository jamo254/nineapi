# main.py
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request

app = FastAPI()

# Mount the "static" directory located within the "nineApi/app" directory
app.mount("/static", StaticFiles(directory="nineApi/app/static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="nineApi/app/templates")

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/user")
def user(request: Request):
    return  templates.TemplateResponse("home.html", {"request": request})