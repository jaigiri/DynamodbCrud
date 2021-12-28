import datetime
import json

import boto3


def lambda_handler(event, context):
    name: str = event['body']['name']
    name = name.strip().title()

    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table('NameTableNames')
    table.put_item(
        Item={
            'initial': name[0],
            'name': name
        }
    )

    return json.dumps(200)
