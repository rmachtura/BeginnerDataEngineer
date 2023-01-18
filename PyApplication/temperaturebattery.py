!pip install boto3

import boto3
import json
import time
from random import uniform
from datetime import datetime

client = boto3.client('kinesis', aws_access_key_id ='', aws_secret_access_key ='', region_name ='')

id = 0
while True:
  data = uniform(19, 27)
  id += 1
  register = {'idtemp' : str(id), 'data': str(data), 'type': 'temperature', 'timestamp': str(datetime.now())}
  client.put_record(StreamName ='', Data = json.dumps(register), PartitionKey='02')
  time.sleep(10)