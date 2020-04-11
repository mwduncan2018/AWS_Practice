"""
Scan reads every item in the table and returns all the data.
Filter the data with an optional FilterExpression.
"""
from __future__ import print_function  # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr


class DecimalEncoder(json.JSONEncoder):
    """Helper class to convert a DynamoDB item to JSON."""
    def default(self, x):
        if isinstance(x, decimal.Decimal):
            if x % 1 > 0:
                return float(x)
            else:
                return int(x)
        return super(DecimalEncoder, self).default(x)


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Guitar')


response = table.scan(
    FilterExpression=Key('brand').eq('Ibanez'),  # get all items where the brand is Ibanez
    ProjectionExpression='model, pickups'  # only return the model field and the pickups field
)

for i in response['Items']:
    print(json.dumps(i, cls=DecimalEncoder))