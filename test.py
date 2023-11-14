import boto3
import os

def s3resource():
    session = boto3.Session(
        aws_access_key_id='e99aee1ec9289d133456583178fad43f',
        aws_secret_access_key='fa2a4f38b83dae484935f557c9c143518246d735f7081dbca4d2dcce99c911cb',
    )
    s3res = session.resource(
        "s3",
        endpoint_url='https://f8ad71970c6794d3992726f550ab5de6.r2.cloudflarestorage.com',
        aws_access_key_id='e99aee1ec9289d133456583178fad43f',
        aws_secret_access_key='fa2a4f38b83dae484935f557c9c143518246d735f7081dbca4d2dcce99c911cb',
    )
    return s3res

def get_cakes(s3):
    ret_list = []
    try:
        bucket = s3.Bucket('cakes')
        files = bucket.objects.all()
        return list(files)
    except:
        print('failed')

s3res = s3resource()
print(get_cakes(s3res))