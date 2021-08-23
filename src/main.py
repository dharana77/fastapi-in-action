from fastapi import FastAPI, Query, Path
from typing import List, Optional, Set
from pydantic import BaseModel, Field
from enum import Enum
from pydantic import BaseModel, HttpUrl, Field

app = FastAPI()

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name : str = Field(..., example="Foo")
    description: Optional[str] = Field(None, example="A very nice Item")
    price: float = Field(..., example=35.4)
    tax: Optional[float] = Field(None, example=3.2)
    
    class Config:
        schema_extra = {
            "example":{
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4
                "tax": 3.2
            }
        }
class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    
class offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]

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

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images

@app.post("/index-weights/")
async def create_index_weigths(weights: Dict[int, float]):
    return weights
