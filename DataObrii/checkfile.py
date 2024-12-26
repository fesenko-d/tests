import boto3

def lambda_handler(event, context):
    s3_resource = boto3.resource('s3')
    my_bucket = s3_resource.Bucket('test-test-1111')
    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)

