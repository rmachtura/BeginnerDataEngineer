!pip install boto3

import boto3
import json
import time
from random import uniform
from datetime import datetime

client = boto3.client('kinesis', aws_access_key_id ='', aws_secret_access_key ='', region_name ='')

id = 0
while True:
  dados = uniform(0.7, 1)
  id += 1
  register = {'idtemp' : str(id), 'data': str(dados), 'type': 'powerfactor', 'timestamp': str(datetime.now())}
  client.put_record(StreamName ='', Data = json.dumps(register), PartitionKey='02')
  time.sleep(10)