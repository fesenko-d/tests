import json
import boto3
import os

def lambda_handler(event, context):
    my_bucket = s3.Bucket('test-test-1111')
    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)
