from fastapi import FastAPI,
from pydantic import BaseModel, Field
from fastapi import Cookie, FastAPI, status
from typing import Optional, Set


app = FastAPI()

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price : float
    tax: Optional[float] = None
    tags: Set[str] = []


@app.post("/items/", response_model = Item, stataus_code = status.HTTP_201_CREATED)
async def create_item(item:Item):
    return item

@app.get("/items/", tags= ["itesm"])
async def read_item():
    return [{"name": "Foo", "price": 42}]

@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]

@app.post(
    "/items/",
    response_model=Item,
    summary="Create an item",
    description="Create an item with all the information, name, description, price"
)
async def create_item(item: Item)
    return item
    