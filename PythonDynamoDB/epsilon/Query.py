"""
The query method is used to retrieve data from a table.
The partition key value is required.
The sort key is optional.

KeyConditionExpression is used to select based on the partition key and sort key
FitlerExpression is used to select based on other attributes
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


def get_all_Ibanez_guitars():
    print('Query to get all Ibanez guitars')
    response = table.query(
        KeyConditionExpression=Key('brand').eq('Ibanez')
    )
    for j in response['Items']:
        print(" : ".join([j['brand'], j['model']]))


def get_all_Ibanez_guitars_with_Dimario_Deactivators():
    print('Query to get all Ibanez where pickups equal "Dimarzio Deactivator Set"')
    response = table.query(
        KeyConditionExpression=Key('brand').eq('Ibanez'),
        FilterExpression=Attr('pickups').eq('Dimarzio Deactivator Set')
    )
    for j in response['Items']:
        print(" : ".join([j['brand'], j['model'], j['pickups']]))


if __name__ == '__main__':
    get_all_Ibanez_guitars()
    get_all_Ibanez_guitars_with_Dimario_Deactivators()
    print('Done...')