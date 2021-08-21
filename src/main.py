from fastapi import FastAPI, Query, Path
from typing import Optional
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name : str
    description : Optional[str] = None
    price: float
    tax: Optional[float] = None

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

app = FastAPI()

@app.post("/items")
async def create_item(q: str = Query("fixedquery", min_length=3)):
    results = {"items": [{"itesm_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.put("items/{item_id}")
async def update_item(
    item_id: int , item:Item, user:User, importance: int = Body(...)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results

