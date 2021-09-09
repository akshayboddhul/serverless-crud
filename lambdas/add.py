import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Employee")


def add(event, context):
    # json.loads method to convert it to json format to object. This phenomenon is known as de-serialization.
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
        # json.dumps method to convert it to object to json format. This phenomenon is known as serialization.
        "body": json.dumps(item)
    }

    return response
