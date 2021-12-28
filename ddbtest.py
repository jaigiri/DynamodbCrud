from pprint import pprint
import boto3


def put_movie(name: str):
    dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    table = dynamodb.Table('NameTableNames')
    response = table.put_item(
        Item={
            'name': name
        }
    )
    return response


if __name__ == '__main__':
    movie_resp = put_movie("winnie win")
    print("Put movie succeeded:")
    pprint(movie_resp, sort_dicts=False)
