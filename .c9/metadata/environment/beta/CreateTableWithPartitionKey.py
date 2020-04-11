{"filter":false,"title":"CreateTableWithPartitionKey.py","tooltip":"/beta/CreateTableWithPartitionKey.py","undoManager":{"mark":97,"position":97,"stack":[[{"start":{"row":0,"column":0},"end":{"row":52,"column":0},"action":"insert","lines":["","#","#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.","#","#  This file is licensed under the Apache License, Version 2.0 (the \"License\").","#  You may not use this file except in compliance with the License. A copy of","#  the License is located at","# ","#  http://aws.amazon.com/apache2.0/","# ","#  This file is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR","#  CONDITIONS OF ANY KIND, either express or implied. See the License for the","#  specific language governing permissions and limitations under the License.","#","from __future__ import print_function # Python 2/3 compatibility","import boto3","","#dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url=\"http://localhost:8000\")","dynamodb = boto3.resource('dynamodb', region_name='us-east-1')","","","table = dynamodb.create_table(","    TableName='YouTubeChannel',","    KeySchema=[","        {","            'AttributeName': 'channel_name',","            'KeyType': 'HASH'  #Partition key","        },","        {","            'AttributeName': 'creator_name',","            'KeyType': 'RANGE'  #Sort key","        }","    ],","    AttributeDefinitions=[","        {","            'AttributeName': 'channel_name',","            'AttributeType': 'S'","        },","        {","            'AttributeName': 'creator_name',","            'AttributeType': 'S'","        },","","    ],","    ProvisionedThroughput={","        'ReadCapacityUnits': 10,","        'WriteCapacityUnits': 10","    }",")","","print(\"Hmmmm?? What is the table status?\")","print(\"Table status:\", table.table_status)",""],"id":1}],[{"start":{"row":1,"column":0},"end":{"row":14,"column":0},"action":"remove","lines":["#","#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.","#","#  This file is licensed under the Apache License, Version 2.0 (the \"License\").","#  You may not use this file except in compliance with the License. A copy of","#  the License is located at","# ","#  http://aws.amazon.com/apache2.0/","# ","#  This file is distributed on an \"AS IS\" BASIS, WITHOUT WARRANTIES OR","#  CONDITIONS OF ANY KIND, either express or implied. See the License for the","#  specific language governing permissions and limitations under the License.","#",""],"id":2}],[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["#"],"id":4}],[{"start":{"row":0,"column":1},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":5},{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"remove","lines":["#"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":2},"action":"insert","lines":["\"\""],"id":6}],[{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["\""],"id":7}],[{"start":{"row":0,"column":3},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":8}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":2},"action":"insert","lines":["\"\""],"id":9}],[{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["\""],"id":10}],[{"start":{"row":0,"column":3},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":11},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["P"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["a"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["r"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["t"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["i"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["t"]},{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":["i"]},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["o"]}],[{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["n"],"id":12}],[{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":[" "],"id":13}],[{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["K"],"id":14},{"start":{"row":1,"column":11},"end":{"row":1,"column":12},"action":"insert","lines":["e"]},{"start":{"row":1,"column":12},"end":{"row":1,"column":13},"action":"insert","lines":["y"]}],[{"start":{"row":1,"column":10},"end":{"row":1,"column":13},"action":"remove","lines":["Key"],"id":15},{"start":{"row":1,"column":10},"end":{"row":1,"column":18},"action":"insert","lines":["KeyError"]}],[{"start":{"row":1,"column":17},"end":{"row":1,"column":18},"action":"remove","lines":["r"],"id":16},{"start":{"row":1,"column":16},"end":{"row":1,"column":17},"action":"remove","lines":["o"]},{"start":{"row":1,"column":15},"end":{"row":1,"column":16},"action":"remove","lines":["r"]},{"start":{"row":1,"column":14},"end":{"row":1,"column":15},"action":"remove","lines":["r"]},{"start":{"row":1,"column":13},"end":{"row":1,"column":14},"action":"remove","lines":["E"]}],[{"start":{"row":1,"column":13},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":17}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"insert","lines":["    "],"id":18}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"remove","lines":["    "],"id":19},{"start":{"row":1,"column":13},"end":{"row":2,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":1,"column":13},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":20},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":[" "]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":[" "]}],[{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":["C"],"id":21},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["o"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["m"]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["p"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":["o"],"id":22},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"remove","lines":["p"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"remove","lines":["m"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"remove","lines":["o"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"remove","lines":["C"]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"remove","lines":[" "]},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"insert","lines":[" "],"id":23},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"insert","lines":[" "]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"insert","lines":[" "]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"insert","lines":["C"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["o"]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["m"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["p"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["o"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["s"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["d"],"id":24}],[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"remove","lines":["d"],"id":25},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["e"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["s"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["o"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":["p"]},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"remove","lines":["m"]},{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"remove","lines":["o"]},{"start":{"row":2,"column":3},"end":{"row":2,"column":4},"action":"remove","lines":["C"]},{"start":{"row":2,"column":2},"end":{"row":2,"column":3},"action":"remove","lines":[" "]},{"start":{"row":2,"column":1},"end":{"row":2,"column":2},"action":"remove","lines":[" "]},{"start":{"row":2,"column":0},"end":{"row":2,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":1,"column":13},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":26}],[{"start":{"row":1,"column":13},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":27}],[{"start":{"row":2,"column":0},"end":{"row":2,"column":4},"action":"insert","lines":["    "],"id":28}],[{"start":{"row":2,"column":4},"end":{"row":2,"column":5},"action":"insert","lines":["C"],"id":29},{"start":{"row":2,"column":5},"end":{"row":2,"column":6},"action":"insert","lines":["o"]},{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["m"]},{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["p"]},{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["o"]},{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["s"]},{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["e"]},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["w"]},{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["d"]}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"remove","lines":["d"],"id":30}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["d"],"id":31}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"remove","lines":["d"],"id":32},{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"remove","lines":["w"]}],[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["d"],"id":33}],[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":[" "],"id":34},{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["o"]},{"start":{"row":2,"column":14},"end":{"row":2,"column":15},"action":"insert","lines":["f"]}],[{"start":{"row":2,"column":15},"end":{"row":2,"column":16},"action":"insert","lines":[" "],"id":35},{"start":{"row":2,"column":16},"end":{"row":2,"column":17},"action":"insert","lines":["o"]},{"start":{"row":2,"column":17},"end":{"row":2,"column":18},"action":"insert","lines":["n"]},{"start":{"row":2,"column":18},"end":{"row":2,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":19},"end":{"row":2,"column":20},"action":"insert","lines":[" "],"id":36},{"start":{"row":2,"column":20},"end":{"row":2,"column":21},"action":"insert","lines":["a"]},{"start":{"row":2,"column":21},"end":{"row":2,"column":22},"action":"insert","lines":["t"]},{"start":{"row":2,"column":22},"end":{"row":2,"column":23},"action":"insert","lines":["t"]},{"start":{"row":2,"column":23},"end":{"row":2,"column":24},"action":"insert","lines":["r"]},{"start":{"row":2,"column":24},"end":{"row":2,"column":25},"action":"insert","lines":["i"]},{"start":{"row":2,"column":25},"end":{"row":2,"column":26},"action":"insert","lines":["b"]},{"start":{"row":2,"column":26},"end":{"row":2,"column":27},"action":"insert","lines":["u"]},{"start":{"row":2,"column":27},"end":{"row":2,"column":28},"action":"insert","lines":["t"]},{"start":{"row":2,"column":28},"end":{"row":2,"column":29},"action":"insert","lines":["e"]}],[{"start":{"row":2,"column":29},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":3,"column":0},"end":{"row":3,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":3,"column":4},"end":{"row":3,"column":5},"action":"insert","lines":["T"],"id":38},{"start":{"row":3,"column":5},"end":{"row":3,"column":6},"action":"insert","lines":["h"]},{"start":{"row":3,"column":6},"end":{"row":3,"column":7},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":7},"end":{"row":3,"column":8},"action":"insert","lines":[" "],"id":39},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["v"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["a"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["l"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["u"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":[" "],"id":40},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["i"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":[" "],"id":41}],[{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"remove","lines":[" "],"id":42},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"remove","lines":["s"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"remove","lines":["i"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"remove","lines":[" "]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["e"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"remove","lines":["u"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"remove","lines":["l"]},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"remove","lines":["a"]},{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"remove","lines":["v"]}],[{"start":{"row":3,"column":8},"end":{"row":3,"column":9},"action":"insert","lines":["k"],"id":43},{"start":{"row":3,"column":9},"end":{"row":3,"column":10},"action":"insert","lines":["e"]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["y"]}],[{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":[" "],"id":44},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["v"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["a"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["l"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["u"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":[" "],"id":45},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["i"]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":[" "],"id":46},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["u"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":["s"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["e"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["d"]}],[{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":[" "],"id":47},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["a"]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":[" "],"id":48},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["i"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":["n"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["p"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["u"]},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":[" "],"id":49}],[{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"remove","lines":[" "],"id":50},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"remove","lines":["t"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"remove","lines":["u"]},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"remove","lines":["p"]},{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"remove","lines":["n"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"remove","lines":["i"]},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"remove","lines":[" "]},{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"remove","lines":["s"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"remove","lines":["a"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"remove","lines":[" "]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"remove","lines":["d"]},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"remove","lines":["e"]},{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"remove","lines":["s"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"remove","lines":["u"]},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"remove","lines":[" "]},{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"remove","lines":["s"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"remove","lines":["i"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"remove","lines":[" "]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"remove","lines":["e"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"remove","lines":["u"]},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"remove","lines":["l"]},{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"remove","lines":["a"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"remove","lines":["v"]},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"remove","lines":[" "]},{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"remove","lines":["y"]}],[{"start":{"row":3,"column":10},"end":{"row":3,"column":11},"action":"insert","lines":["y"],"id":51},{"start":{"row":3,"column":11},"end":{"row":3,"column":12},"action":"insert","lines":["'"]},{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":[" "],"id":52},{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["v"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["a"]},{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["l"]},{"start":{"row":3,"column":17},"end":{"row":3,"column":18},"action":"insert","lines":["u"]},{"start":{"row":3,"column":18},"end":{"row":3,"column":19},"action":"insert","lines":["e"]}],[{"start":{"row":3,"column":19},"end":{"row":3,"column":20},"action":"insert","lines":[" "],"id":53},{"start":{"row":3,"column":20},"end":{"row":3,"column":21},"action":"insert","lines":["i"]},{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":22},"end":{"row":3,"column":23},"action":"insert","lines":[" "],"id":54},{"start":{"row":3,"column":23},"end":{"row":3,"column":24},"action":"insert","lines":["u"]},{"start":{"row":3,"column":24},"end":{"row":3,"column":25},"action":"insert","lines":["s"]},{"start":{"row":3,"column":25},"end":{"row":3,"column":26},"action":"insert","lines":["e"]},{"start":{"row":3,"column":26},"end":{"row":3,"column":27},"action":"insert","lines":["d"]}],[{"start":{"row":3,"column":27},"end":{"row":3,"column":28},"action":"insert","lines":[" "],"id":55},{"start":{"row":3,"column":28},"end":{"row":3,"column":29},"action":"insert","lines":["a"]},{"start":{"row":3,"column":29},"end":{"row":3,"column":30},"action":"insert","lines":["s"]}],[{"start":{"row":3,"column":30},"end":{"row":3,"column":31},"action":"insert","lines":[" "],"id":56},{"start":{"row":3,"column":31},"end":{"row":3,"column":32},"action":"insert","lines":["i"]},{"start":{"row":3,"column":32},"end":{"row":3,"column":33},"action":"insert","lines":["n"]},{"start":{"row":3,"column":33},"end":{"row":3,"column":34},"action":"insert","lines":["p"]},{"start":{"row":3,"column":34},"end":{"row":3,"column":35},"action":"insert","lines":["u"]},{"start":{"row":3,"column":35},"end":{"row":3,"column":36},"action":"insert","lines":["t"]}],[{"start":{"row":3,"column":36},"end":{"row":3,"column":37},"action":"insert","lines":[" "],"id":57},{"start":{"row":3,"column":37},"end":{"row":3,"column":38},"action":"insert","lines":["t"]},{"start":{"row":3,"column":38},"end":{"row":3,"column":39},"action":"insert","lines":["o"]}],[{"start":{"row":3,"column":39},"end":{"row":3,"column":40},"action":"insert","lines":[" "],"id":58},{"start":{"row":3,"column":40},"end":{"row":3,"column":41},"action":"insert","lines":["a"]},{"start":{"row":3,"column":41},"end":{"row":3,"column":42},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":42},"end":{"row":3,"column":43},"action":"insert","lines":[" "],"id":59},{"start":{"row":3,"column":43},"end":{"row":3,"column":44},"action":"insert","lines":["i"]},{"start":{"row":3,"column":44},"end":{"row":3,"column":45},"action":"insert","lines":["n"]},{"start":{"row":3,"column":45},"end":{"row":3,"column":46},"action":"insert","lines":["t"]},{"start":{"row":3,"column":46},"end":{"row":3,"column":47},"action":"insert","lines":["e"]},{"start":{"row":3,"column":47},"end":{"row":3,"column":48},"action":"insert","lines":["r"]},{"start":{"row":3,"column":48},"end":{"row":3,"column":49},"action":"insert","lines":["n"]},{"start":{"row":3,"column":49},"end":{"row":3,"column":50},"action":"insert","lines":["a"]},{"start":{"row":3,"column":50},"end":{"row":3,"column":51},"action":"insert","lines":["l"]}],[{"start":{"row":3,"column":51},"end":{"row":3,"column":52},"action":"insert","lines":[" "],"id":60},{"start":{"row":3,"column":52},"end":{"row":3,"column":53},"action":"insert","lines":["h"]},{"start":{"row":3,"column":53},"end":{"row":3,"column":54},"action":"insert","lines":["a"]},{"start":{"row":3,"column":54},"end":{"row":3,"column":55},"action":"insert","lines":["s"]},{"start":{"row":3,"column":55},"end":{"row":3,"column":56},"action":"insert","lines":["h"]}],[{"start":{"row":3,"column":56},"end":{"row":3,"column":57},"action":"insert","lines":[" "],"id":61},{"start":{"row":3,"column":57},"end":{"row":3,"column":58},"action":"insert","lines":["f"]},{"start":{"row":3,"column":58},"end":{"row":3,"column":59},"action":"insert","lines":["u"]},{"start":{"row":3,"column":59},"end":{"row":3,"column":60},"action":"insert","lines":["c"]},{"start":{"row":3,"column":60},"end":{"row":3,"column":61},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":60},"end":{"row":3,"column":61},"action":"remove","lines":["n"],"id":62},{"start":{"row":3,"column":59},"end":{"row":3,"column":60},"action":"remove","lines":["c"]}],[{"start":{"row":3,"column":59},"end":{"row":3,"column":60},"action":"insert","lines":["n"],"id":63},{"start":{"row":3,"column":60},"end":{"row":3,"column":61},"action":"insert","lines":["c"]},{"start":{"row":3,"column":61},"end":{"row":3,"column":62},"action":"insert","lines":["t"]},{"start":{"row":3,"column":62},"end":{"row":3,"column":63},"action":"insert","lines":["i"]},{"start":{"row":3,"column":63},"end":{"row":3,"column":64},"action":"insert","lines":["o"]},{"start":{"row":3,"column":64},"end":{"row":3,"column":65},"action":"insert","lines":["n"]}],[{"start":{"row":3,"column":65},"end":{"row":4,"column":0},"action":"insert","lines":["",""],"id":64},{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["M"]}],[{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["u"],"id":65},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["s"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":[" "],"id":66},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["b"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":[" "],"id":67}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"remove","lines":[" "],"id":68},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"remove","lines":["e"]},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"remove","lines":["b"]},{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"remove","lines":[" "]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"remove","lines":["t"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"remove","lines":["s"]},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"remove","lines":["u"]},{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"remove","lines":["M"]}],[{"start":{"row":4,"column":4},"end":{"row":4,"column":5},"action":"insert","lines":["M"],"id":69},{"start":{"row":4,"column":5},"end":{"row":4,"column":6},"action":"insert","lines":["u"]},{"start":{"row":4,"column":6},"end":{"row":4,"column":7},"action":"insert","lines":["s"]},{"start":{"row":4,"column":7},"end":{"row":4,"column":8},"action":"insert","lines":["t"]}],[{"start":{"row":4,"column":8},"end":{"row":4,"column":9},"action":"insert","lines":[" "],"id":70},{"start":{"row":4,"column":9},"end":{"row":4,"column":10},"action":"insert","lines":["b"]},{"start":{"row":4,"column":10},"end":{"row":4,"column":11},"action":"insert","lines":["e"]}],[{"start":{"row":4,"column":11},"end":{"row":4,"column":12},"action":"insert","lines":[" "],"id":71}],[{"start":{"row":4,"column":12},"end":{"row":4,"column":13},"action":"insert","lines":["a"],"id":72},{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"remove","lines":["s"],"id":73}],[{"start":{"row":4,"column":13},"end":{"row":4,"column":14},"action":"insert","lines":[" "],"id":74},{"start":{"row":4,"column":14},"end":{"row":4,"column":15},"action":"insert","lines":["s"]},{"start":{"row":4,"column":15},"end":{"row":4,"column":16},"action":"insert","lines":["t"]},{"start":{"row":4,"column":16},"end":{"row":4,"column":17},"action":"insert","lines":["r"]},{"start":{"row":4,"column":17},"end":{"row":4,"column":18},"action":"insert","lines":["i"]},{"start":{"row":4,"column":18},"end":{"row":4,"column":19},"action":"insert","lines":["n"]},{"start":{"row":4,"column":19},"end":{"row":4,"column":20},"action":"insert","lines":["g"]},{"start":{"row":4,"column":20},"end":{"row":4,"column":21},"action":"insert","lines":[","]}],[{"start":{"row":4,"column":21},"end":{"row":4,"column":22},"action":"insert","lines":[" "],"id":75},{"start":{"row":4,"column":22},"end":{"row":4,"column":23},"action":"insert","lines":["a"]}],[{"start":{"row":4,"column":23},"end":{"row":4,"column":24},"action":"insert","lines":[" "],"id":76},{"start":{"row":4,"column":24},"end":{"row":4,"column":25},"action":"insert","lines":["n"]},{"start":{"row":4,"column":25},"end":{"row":4,"column":26},"action":"insert","lines":["u"]},{"start":{"row":4,"column":26},"end":{"row":4,"column":27},"action":"insert","lines":["m"]},{"start":{"row":4,"column":27},"end":{"row":4,"column":28},"action":"insert","lines":["b"]},{"start":{"row":4,"column":28},"end":{"row":4,"column":29},"action":"insert","lines":["e"]},{"start":{"row":4,"column":29},"end":{"row":4,"column":30},"action":"insert","lines":["r"]},{"start":{"row":4,"column":30},"end":{"row":4,"column":31},"action":"insert","lines":[","]}],[{"start":{"row":4,"column":31},"end":{"row":4,"column":32},"action":"insert","lines":[" "],"id":77},{"start":{"row":4,"column":32},"end":{"row":4,"column":33},"action":"insert","lines":["o"]},{"start":{"row":4,"column":33},"end":{"row":4,"column":34},"action":"insert","lines":["r"]}],[{"start":{"row":4,"column":34},"end":{"row":4,"column":35},"action":"insert","lines":[" "],"id":78},{"start":{"row":4,"column":35},"end":{"row":4,"column":36},"action":"insert","lines":["b"]},{"start":{"row":4,"column":36},"end":{"row":4,"column":37},"action":"insert","lines":["i"]},{"start":{"row":4,"column":37},"end":{"row":4,"column":38},"action":"insert","lines":["n"]},{"start":{"row":4,"column":38},"end":{"row":4,"column":39},"action":"insert","lines":["a"]},{"start":{"row":4,"column":39},"end":{"row":4,"column":40},"action":"insert","lines":["r"]},{"start":{"row":4,"column":40},"end":{"row":4,"column":41},"action":"insert","lines":["y"]}],[{"start":{"row":4,"column":41},"end":{"row":5,"column":0},"action":"insert","lines":["",""],"id":79},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":6,"column":3},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":80}],[{"start":{"row":4,"column":41},"end":{"row":5,"column":4},"action":"remove","lines":["","    "],"id":81}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":29},"action":"remove","lines":["YouTubeChannel"],"id":82}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["H"],"id":83},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["e"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["a"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["d"]}],[{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["p"],"id":84},{"start":{"row":15,"column":20},"end":{"row":15,"column":21},"action":"insert","lines":["h"]},{"start":{"row":15,"column":21},"end":{"row":15,"column":22},"action":"insert","lines":["o"]},{"start":{"row":15,"column":22},"end":{"row":15,"column":23},"action":"insert","lines":["n"]},{"start":{"row":15,"column":23},"end":{"row":15,"column":24},"action":"insert","lines":["e"]},{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":["s"]}],[{"start":{"row":18,"column":41},"end":{"row":18,"column":42},"action":"remove","lines":["e"],"id":85},{"start":{"row":18,"column":40},"end":{"row":18,"column":41},"action":"remove","lines":["m"]},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"remove","lines":["a"]},{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"remove","lines":["n"]},{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"remove","lines":["_"]},{"start":{"row":18,"column":36},"end":{"row":18,"column":37},"action":"remove","lines":["l"]},{"start":{"row":18,"column":35},"end":{"row":18,"column":36},"action":"remove","lines":["e"]},{"start":{"row":18,"column":34},"end":{"row":18,"column":35},"action":"remove","lines":["n"]},{"start":{"row":18,"column":33},"end":{"row":18,"column":34},"action":"remove","lines":["n"]},{"start":{"row":18,"column":32},"end":{"row":18,"column":33},"action":"remove","lines":["a"]},{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"remove","lines":["h"]},{"start":{"row":18,"column":30},"end":{"row":18,"column":31},"action":"remove","lines":["c"]}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":25},"action":"remove","lines":["Headphones"],"id":86}],[{"start":{"row":15,"column":15},"end":{"row":15,"column":16},"action":"insert","lines":["S"],"id":87},{"start":{"row":15,"column":16},"end":{"row":15,"column":17},"action":"insert","lines":["t"]},{"start":{"row":15,"column":17},"end":{"row":15,"column":18},"action":"insert","lines":["a"]},{"start":{"row":15,"column":18},"end":{"row":15,"column":19},"action":"insert","lines":["t"]},{"start":{"row":15,"column":19},"end":{"row":15,"column":20},"action":"insert","lines":["e"]}],[{"start":{"row":18,"column":30},"end":{"row":18,"column":31},"action":"insert","lines":["s"],"id":88},{"start":{"row":18,"column":31},"end":{"row":18,"column":32},"action":"insert","lines":["t"]},{"start":{"row":18,"column":32},"end":{"row":18,"column":33},"action":"insert","lines":["a"]},{"start":{"row":18,"column":33},"end":{"row":18,"column":34},"action":"insert","lines":["t"]},{"start":{"row":18,"column":34},"end":{"row":18,"column":35},"action":"insert","lines":["e"]},{"start":{"row":18,"column":35},"end":{"row":18,"column":36},"action":"insert","lines":["_"]},{"start":{"row":18,"column":36},"end":{"row":18,"column":37},"action":"insert","lines":["n"]},{"start":{"row":18,"column":37},"end":{"row":18,"column":38},"action":"insert","lines":["a"]},{"start":{"row":18,"column":38},"end":{"row":18,"column":39},"action":"insert","lines":["m"]},{"start":{"row":18,"column":39},"end":{"row":18,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":21,"column":0},"end":{"row":25,"column":0},"action":"remove","lines":["        {","            'AttributeName': 'creator_name',","            'KeyType': 'RANGE'  #Sort key","        }",""],"id":89}],[{"start":{"row":27,"column":0},"end":{"row":32,"column":0},"action":"remove","lines":["        {","            'AttributeName': 'creator_name',","            'AttributeType': 'S'","        },","",""],"id":90}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":42},"action":"remove","lines":["channel_name"],"id":91}],[{"start":{"row":24,"column":30},"end":{"row":24,"column":31},"action":"insert","lines":["s"],"id":92},{"start":{"row":24,"column":31},"end":{"row":24,"column":32},"action":"insert","lines":["t"]},{"start":{"row":24,"column":32},"end":{"row":24,"column":33},"action":"insert","lines":["a"]},{"start":{"row":24,"column":33},"end":{"row":24,"column":34},"action":"insert","lines":["t"]},{"start":{"row":24,"column":34},"end":{"row":24,"column":35},"action":"insert","lines":["e"]},{"start":{"row":24,"column":35},"end":{"row":24,"column":36},"action":"insert","lines":["_"]},{"start":{"row":24,"column":36},"end":{"row":24,"column":37},"action":"insert","lines":["n"]},{"start":{"row":24,"column":37},"end":{"row":24,"column":38},"action":"insert","lines":["a"]},{"start":{"row":24,"column":38},"end":{"row":24,"column":39},"action":"insert","lines":["m"]},{"start":{"row":24,"column":39},"end":{"row":24,"column":40},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":0},"end":{"row":34,"column":42},"action":"remove","lines":["print(\"Hmmmm?? What is the table status?\")"],"id":93}],[{"start":{"row":33,"column":0},"end":{"row":34,"column":0},"action":"remove","lines":["",""],"id":94}],[{"start":{"row":34,"column":7},"end":{"row":34,"column":8},"action":"insert","lines":["S"],"id":95},{"start":{"row":34,"column":8},"end":{"row":34,"column":9},"action":"insert","lines":["t"]},{"start":{"row":34,"column":9},"end":{"row":34,"column":10},"action":"insert","lines":["a"]},{"start":{"row":34,"column":10},"end":{"row":34,"column":11},"action":"insert","lines":["t"]},{"start":{"row":34,"column":11},"end":{"row":34,"column":12},"action":"insert","lines":["e"]}],[{"start":{"row":34,"column":12},"end":{"row":34,"column":13},"action":"insert","lines":[" "],"id":96}],[{"start":{"row":34,"column":18},"end":{"row":34,"column":19},"action":"insert","lines":["'"],"id":97}],[{"start":{"row":34,"column":7},"end":{"row":34,"column":8},"action":"insert","lines":["'"],"id":98}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":35,"column":0},"end":{"row":35,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1586303221472,"hash":"5fbb0396b0daedb023b60c387a958116b16f3a86"}