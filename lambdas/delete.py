import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Employee")


def delete(event, context):
    table.delete_item(Key={'id': event['pathParameters']['id']})
    response = {
        "statusCode": 200
    }

    return response
