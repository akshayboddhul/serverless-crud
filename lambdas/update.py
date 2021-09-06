import json
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Employee")


def update(event, context):
    data = json.loads(event['body'])

    result = table.update_item(Key={'id': event['pathParameters']['id']},
                               ExpressionAttributeNames={
        '#emp_name': 'Name'
    },
        ExpressionAttributeValues={
        ':Name': data['Name']
    },
        UpdateExpression='SET #emp_name = :Name',
        ReturnValues='ALL_NEW',
    )

    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'])
    }

    return response
