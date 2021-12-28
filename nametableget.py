import boto3


def lambda_handler(event, context):
    s3 = boto3.resource('s3')

    obj = s3.Object("nametable", "index.html")
    page_content = obj.get()['Body'].read().decode('utf-8')
    return page_content
