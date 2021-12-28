import boto3


def lambda_handler(event, context):
    html = """
    <!-- pure.edit.get -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Edit</title>
</head>
<body>
<form method="post" action="https://cmjvj39cxk.execute-api.us-west-2.amazonaws.com/Prod/pure/edit">
    <input type="submit" value="Save">
    {{ WATO WAI }}
</form>
</body>
</html>
    """

    input_elem = "<input type=\"text\" name=\"{{ YAY }}\" value=\"{{ YAY }}\">"
    input_elems = ""

    dynamo_client = boto3.client("dynamodb", region_name='us-west-2')
    paginator = dynamo_client.get_paginator("scan")

    for page in paginator.paginate(TableName="NameTableNames"):
        for i in [item['name']['S'] for item in page["Items"]]:
            input_elems += input_elem.replace("{{ YAY }}", i)

    return html.replace("{{ WATO WAI }}", input_elems)
