import json

import boto3


def lambda_handler(event, context):
    namep = event['body']['name']
    name, new_name = namep
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table('NameTableNames')

    table.delete_item(
        Key={
            'initial': name[0],
            'name': name
        }
    )

    table.put_item(
        Item={
            'initial': new_name[0],
            'name': new_name
        }
    )

    return json.dumps(200)
