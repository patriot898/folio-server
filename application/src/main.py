import os
from dotenv import load_dotenv
from typing import Union
from .dal import connect
from .dal.proc_calls import users

from fastapi import FastAPI
from fastapi_sessions import SessionManager

SESSION_KEY = os.getenv('SECRET_KEY')
SESSION_COOKIE = os.getenv('SESSION_COOKIE_NAME')

app = FastAPI()
connector = connect.DBConnector()
session_manager = SessionManager(
    secret_key=SESSION_KEY,
    session_cookie=SESSION_COOKIE
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users")
def get_user(username: str, password: str):
    row = users.user_get(connector, username, password)

@app.post("/login")
async def login(username: str, password: str):
    row = users.user_get(connector, username, password)
    session = await session_manager.create_session()
    session['user'] = username


@app.post('/manual_connect/')
def deploy_directory(directory: str):
    connector.deploy_directory(directory)




