import boto3
import os

def s3resource():
    session = boto3.Session(
        aws_access_key_id='8699d5b5b7ac38beec3066e254a21f00',
        aws_secret_access_key='e467d4b8adfd79d9287ee9c32d8fc7bd47cd38a5a1bd8d04fe2fe1e82dd63695',
    )
    s3res = session.resource(
        "s3",
        endpoint_url='https://f8ad71970c6794d3992726f550ab5de6.r2.cloudflarestorage.com',
        aws_access_key_id='8699d5b5b7ac38beec3066e254a21f00',
        aws_secret_access_key='e467d4b8adfd79d9287ee9c32d8fc7bd47cd38a5a1bd8d04fe2fe1e82dd63695',
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