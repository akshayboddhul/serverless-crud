import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Employee")


def hello(event, context):
    emp = table.scan()['Items']
    body = {
        "statusCode": 200,
        "message": "Go Serverless v2.0! Your function executed successfully!",
        "body": emp
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
