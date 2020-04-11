from __future__ import print_function  # Python 2/3 compatibility

import json
import decimal

import boto3
from botocore.exceptions import ClientError


class DecimalEncoder(json.JSONEncoder):
    """Helper class to convert a DynamoDB item to JSON."""
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if abs(o) % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table= dynamodb.Table('Guitar')


def put_guitar(brand, model, pickups):
    table.put_item(
        Item={
            'brand': brand,
            'model': model,
            'pickups': pickups
        })
        

def put_guitar_if_does_not_exist(brand, model, pickups):
    table.put_item(
        Item={
            'brand': brand,
            'model': model,
            'pickups': pickups
        },
        ConditionExpression = 'attribute_not_exists(brand)')


def get_guitar(brand, model):
    try:
        response = table.get_item(
            Key={
                'brand': brand,
                'model': model
            })
        item = response['Item']
        print(', '.join(['get', brand, model, 'successful get']))
        print(json.dumps(item, indent=4, cls=DecimalEncoder))
    except:
            print(', '.join(['get', brand, model, 'ERROR during get']))


def update_guitar(brand, model, pickups):
    response = table.update_item(
        Key={
            'brand': brand,
            'model': model
        },
        UpdateExpression='set pickups = :p',
        ExpressionAttributeValues={
            ':p': pickups
        },
        ReturnValues="UPDATED_NEW"
    )


def increment_guitar(brand, model):
    response = table.update_item(
        Key={
            'brand': brand,
            'model': model
        },
        UpdateExpression='set rating = rating + :val',
        ExpressionAttributeValues={
            ':val': decimal.Decimal(1)
        },
        ReturnValues='UPDATED_NEW'
    )
    print('Incremented ' + str(brand) + ' ' + str(model))
    print(json.dumps(response, indent=4, cls=DecimalEncoder))


def decrement_guitar(brand, model):
    response = table.update_item(
        Key={
            'brand': brand,
            'model': model
        },
        UpdateExpression='set rating = rating - :val',
        ExpressionAttributeValues={
            ':val': decimal.Decimal(1)
        },
        ReturnValues='UPDATED_NEW'
    )
    print('Decremented ' + str(brand) + ' ' + str(model))
    print(json.dumps(response, indent=4, cls=DecimalEncoder))


def conditional_update_guitar(brand, model):
    try:
        response = table.update_item(
            Key={
                'brand': brand,
                'model': model
            },
            UpdateExpression = 'set rating = :val',
            ConditionExpression = 'rating > :upperbound OR rating < :lowerbound',
            ExpressionAttributeValues={
                ':val': decimal.Decimal(0),
                ':upperbound': decimal.Decimal(3),
                ':lowerbound': decimal.Decimal(-3)
            },
            ReturnValues = 'UPDATED_NEW')
        print('Conditional Update Guitar Succeeded')
        print(json.dumps(response, indent=4, cls=DecimalEncoder))
    except ClientError as e:
        if e.response['Error']['Code'] == 'ConditionalCheckFailedException':
            print(e.response['Error']['Message'])
        else:
            raise


def delete_guitar(brand, model):
    try:
        response = table.delete_item(
            Key={
                'brand': brand,
                'model': model
            })
        print("Delete Guitar Succeeded")
        print(json.dumps(response, indent=4, cls=DecimalEncoder))
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            print('Delete Guitar Failed --> The next line should mention a conditional request failure')


if __name__ == '__main__':
    update_guitar('Ibanez', 'Prestige RG', 'Dimarzio Deactivator Set')
    get_guitar('Ibanez', 'Prestige RG')
    
    increment_guitar('ESP', 'Eclipse')
    decrement_guitar('BC Rich', 'Warlock')
    
    
    put_guitar('LTD', 'Horizon', 'Bare Knuckle Holy Diver')
    delete_guitar('LTD', 'Horizon')
    
    if table.get_item(Key={'brand': 'BC Rich','model': 'Warlock'})['Item']['rating'] < -3:
        print('BC Rich Warlock\'s rating is less than -3')
        conditional_update_guitar('BC Rich', 'Warlock')
    else:
        print('BC Rich Warlock\'s rating is not less than 3')
    
    if table.get_item(Key={'brand':'ESP','model':'Eclipse'})['Item']['rating'] > 3:
        print('ESP Eclipse\'s rating is greater than 3')
        conditional_update_guitar('ESP', 'Eclipse')
    else:
        print('ESP Eclipse\'s rating is not greater than 3')
        
    print('Done...')
    
    delete_guitar('Fender', 'Tele')
    put_guitar_if_does_not_exist('Fender', 'Tele', 'Stock')