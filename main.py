from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


items = []


@app.get("/")
def read_root():
    return {"hello": "world"}


@app.get("/items")
def get_items():
    return items


@app.get('/items/{item_id}')
def get_item(item_id: int, q: Union[str, None] = None):
    if item_id >= len(items):
        return None
    return items[item_id]


@app.post('/items/')
def post_item(item: Item):
    items.append({len(items): item})
    return {"message": "Success"}


@app.put("/items/{item_id}")
def put_item(item: Item, item_id: int):
    items[item_id] = item
    return items[item_id]
