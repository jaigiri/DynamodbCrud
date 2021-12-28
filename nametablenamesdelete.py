import json

import boto3


def lambda_handler(event, context):
    name = event['body']['name']
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table('NameTableNames')

    table.delete_item(
        Key={
            'initial': name[0],
            'name': name
        }
    )

    return json.dumps(200)
