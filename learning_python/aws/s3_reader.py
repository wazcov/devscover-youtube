#! /usr/local/bin/python3

import boto3
import os

s3 = None

def login():
    global s3
    aws_session = boto3.Session(profile_name=os.environ['AWS_PROFILE'])
    s3 = aws_session.client('s3')
    return s3

def list_buckets():
    global s3
    response = s3.list_buckets()
    bucket_list = {}
    for i, bucket in enumerate(response['Buckets']):
        bucket_list[i] = bucket['Name']
        print(f"{i} - {bucket_list[i]}")
    bucket_id = input("\nChoose A Bucket:")
    try:
        bucket_name = bucket_list[int(bucket_id)]
    except:
        print("Not A Bucket ID")
        exit(-1)
    return bucket_name

def list_objects(bucket_name):
    global s3
    objects = s3.list_objects_v2(Bucket=bucket_name)
    object_list = {}
    for i, item in enumerate(objects['Contents']):
        object_list[i] = item['Key']
        print(f"{i} - {object_list[i]}")
    obj_id = input("\nChoose An Item:")
    try:
        obj_name =  object_list[int(obj_id)]
    except:
        print("Not An Item ID")
        exit(-1)
    return obj_name

def retrieve_s3_file():
    s3 = login()
    bucket_name = list_buckets()

    print(f"\nUsing bucket: {bucket_name}\n")

    object_name = list_objects(bucket_name)

    print(f"\nDownloading Item: {object_name}\n")

    filename = f"./downloads/{object_name}"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as f:
        s3.download_fileobj(bucket_name, object_name, f)

if __name__ == "__main__":
    retrieve_s3_file()