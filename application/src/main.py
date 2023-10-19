from typing import Union
from .dal import connect
from .dal.proc_calls import users

from fastapi import FastAPI

app = FastAPI()
connector = connect.DBConnector()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/users")
def get_user(username: str, password: str):
    row = users.user_get(connector, username, password)

@app.post('/manual_connect/')
def deploy_directory(directory: str):
    connector.deploy_directory(directory)




