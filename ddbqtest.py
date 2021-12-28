import boto3


def scan_table(table_name: str, **kwargs):
    dynamo_client = boto3.client("dynamodb", region_name='us-west-2')
    paginator = dynamo_client.get_paginator("scan")

    for page in paginator.paginate(TableName=table_name, **kwargs):
        yield [item['name']['S'] for item in page["Items"]]


if __name__ == "__main__":
    for item in scan_table(table_name="NameTableNames"):
        print(item)
