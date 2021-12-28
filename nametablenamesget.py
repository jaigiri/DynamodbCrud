import json
import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')
    table = dynamodb.Table('NameTableNames')
    items = []

    query_str = event['body']['query']
    if len(query_str) > 0:
        response = table.query(
            KeyConditionExpression=Key('initial').eq(query_str[0]) & Key('name').begins_with(query_str)
        )
        for item in response['Items']:
            items.append(item['name'])
    else:
        for item in table.scan()['Items']:
            items.append(item['name'])

    return json.dumps(items)
