import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Employee")


def add(event, context):
    data = json.loads(event['body'])
    print("BODYDATA:", data)
    item = {
        'id': data['id'],
        'Name': data['Name']
    }
    print("ITEM:", item)
    table.put_item(Item=item)
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
