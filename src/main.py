from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name : str
    price: float
    is_offer: Optional[bool] = None

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q":q}

@app.put("/items/{items_id}")
def update_item(item_id:int, item:Item):
    return {"item_name": item.name, "item_id":item_id}

@app.get("users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id")
async def read_user(user_id:str):
    return {"user_id": user_id}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"mdoel_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value =="lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
