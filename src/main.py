from fastapi import FastAPI,
from pydantic import BaseModel, Field
from fastapi import Cookie, FastAPI
from typing import Union, List, Dict

class BaseItem(BaseModel):
    description: str
    type: str

class CarItem(BaseItem):
    type = "car"

class PlaneItem(BaseItem):
    type = "plane"
    size: int

class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description:str

class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    
class Offer(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    items: List[Item]

class UserBase(BaseModel):
    username: str
    full_name: Optional[str] = None

class UserIn(UserBase):
    password: str

class UserOUt(UserBase):
    pass

class UserInDB(UserBase):
    hashed_password: str

def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password

def fake_sava_user(user_in: UserIn):
    hashed_password = fake_password_hashser(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User save! not really.")
    return user_in_db


app = FastAPI()


@app.post("/items", response_model=List[Item])
async def read_items():
    return items

@app.post("/user", response_model=UserOut)
async def create_user(user: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

@app.put("items/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_item(item_id : str):
    return items[item_id]

@app.post("/offers/")
async def create_offer(offer: Offer):
    return offer

@app.post("/images/multiple/")
async def create_multiple_images(images: List[Image]):
    return images

@app.post("/index-weights/")
async def create_index_weigths(weights: dict[int, float]):
    return weights

@app.get("/keyword-weights/", response_model=Dict[str,float])
async def read_keyword_weights():
    return {"foo":2.3, "bar": 3.4}
    