from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

table = dynamodb.Table('Guitar')

table.put_item(
    Item={
        'brand': 'ESP',
        'model': 'Horizon',
        'pickups': 'Seymour JB/59'
    })
    
table.put_item(
    Item={
        'brand': 'ESP',
        'model': 'M-II',
        'pickups': 'EMG 57/66'
    })
    
table.put_item(
    Item={
        'brand': 'Ibanez',
        'model': 'Iron Label RG',
        'pickups': 'Dimarzio Edge Fusion Set'
    })
    