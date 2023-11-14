from typing import Union
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel
import os
from lib import get_next_id, add_cake_to_s3, s3client, delete_cake_from_s3, get_cakes, s3resource

app = FastAPI()


class Cake(BaseModel):
    name: str
    comment: str
    image_url: str
    yum_factor: int  # we should validate this value as it needs to be between 1-5


@app.get("/items/")
async def read_items():
    # initiate s3 client
    s3res = s3resource()
    # read all files in S3 bucket
    cakes_list = get_cakes(s3res)
    # build a list of cakes
    return os.environ["cf_endpoint"]
    return cakes_list


@app.post("/items/add/")
async def add_items(cake: Cake):
    # initiate s3 client
    s3 = s3client()
    # get the id and use that as the filename in S3
    id = get_next_id(s3)
    # write the cake to the json file in s3
    result = add_cake_to_s3(s3, id, cake)
    # return the result
    return result


@app.delete("/items/delete/{item_id}")
async def delete_items(item_id: str):
    # find s3 file with name based on ID and delete it
    if item_id != 'id':
        s3 = s3client()
        key = item_id + '.json'
        return delete_cake_from_s3
    


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
