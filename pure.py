import boto3


def lambda_handler(event, context):
    html = """
    <!-- pure.get -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Names</title>
</head>
<body>
<a href="https://cmjvj39cxk.execute-api.us-west-2.amazonaws.com/Prod/pure/edit">Edit names</a>
<ul>
    {{ WATO WAI }}
</ul>
</body>
</html>
    """

    li_elem = "<li>{{ YAY }}</li>"
    li_elems = ""

    dynamo_client = boto3.client("dynamodb", region_name='us-west-2')
    paginator = dynamo_client.get_paginator("scan")

    for page in paginator.paginate(TableName="NameTableNames"):
        for i in [item['name']['S'] for item in page["Items"]]:
            li_elems += li_elem.replace("{{ YAY }}", i)

    print(li_elems)
    return html.replace("{{ WATO WAI }}", li_elems)
