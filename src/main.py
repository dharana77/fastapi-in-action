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

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.post("/items")
async def create_item(q: str = Query("fixedquery", min_length=3)):
    results = {"items": [{"itesm_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("items/{item_id}")
async def read_items(
    item_id : int = Path(..., title= "The Id of the item to get")
    q : Optional[str] = Query(None, alias = "item-query"),
):
    results = {"item_id" : item_id}
    if q:
        resulsts.update({"q": q})
    
    return results

