import boto3
import os
import json
from botocore.exceptions import ClientError
import logging

BUCKET = "cakes"
INDEX_FILE = "ids.json"


def s3client():
    s3 = boto3.client(
        service_name="s3",
        endpoint_url=os.environ["cf_endpoint"],
        aws_access_key_id=os.environ["cf_api_key"],
        aws_secret_access_key=os.environ["cf_api_secret"],
        region_name="auto",  # Must be one of: wnam, enam, weur, eeur, apac, auto
    )
    return s3


def get_file(s3, filename):
    file = s3.get_object(Bucket=BUCKET, Key=filename)["Body"].read()
    return file


def create_index(s3):
    file_name = "config.json"
    s3.upload_file(file_name, BUCKET, INDEX_FILE)


def get_next_id(s3):
    try:
        last_id = s3.get_object(Bucket=BUCKET, Key=INDEX_FILE)["Body"].read()
        return last_id
        next_id = int(last_id["last_client_id"]) + 1
        return next_id
    except:
        # must be a brand new system so lets initiate the ids file by copying it from local
        create_index(s3)
        last_id = s3.get_object(Bucket=BUCKET, Key=INDEX_FILE)["Body"].read()
        next_id = int(last_id["last_client_id"]) + 1
        return next_id


def add_cake_to_s3(s3, id, cake):
    try:
        s3.put_object(Body=json.dumps(cake), Bucket=BUCKET, Key=id + ".json")
        last_id = {"last_clientid": id}
    except ClientError as e:
        logging.error(e)
        return {"Status": "Failed"}
    return {"Status": "Success"}


def delete_cake_from_s3(id):
    return {"Status": "Deleted"}
