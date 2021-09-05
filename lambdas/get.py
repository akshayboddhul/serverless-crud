import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Employee")


def get(event, context):
    emp = table.get_item(Key={'id': event['pathParameters']['id']})
    print("EMP:", emp)
    response = {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(emp['Item'])
    }

    return response
