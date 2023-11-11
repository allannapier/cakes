from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

app = FastAPI()

class Cake(BaseModel):
    id : int
    name: str
    comment: str
    image_url: str
    yum_factor: int #we should validate this value as it needs to be between 1-5


@app.get("/items/")
async def read_items():
    return [{"name": "Foo"}]

@app.post("/items/add/")
async def add_items( cake: Cake,):
    return [{"name": "cake1"}]

@app.delete("/items/delete/{item_id}")
async def delete_items():
    return [{"name": "Foo"}]


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Cake Stall API",
        version="0.0.1",
        summary="This is an api for cakes",
        description="Use this api to view our cakes, add new and delete old cakes",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://cakesburg.co.uk/cdn/shop/products/happy-birthday-topper-drip-cake-30_800x.jpg?v=16043539375"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi
