import boto3
import botocore
import os
import csv

def run(bucket_name, file_name):

    ACCESS_KEY_ID = os.environ['ACCESS_KEY_ID']
    SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']

    client = boto3.client('s3', aws_access_key_id=ACCESS_KEY_ID, aws_secret_access_key=SECRET_ACCESS_KEY)

    response = client.get_object(Bucket=bucket_name, Key=file_name, ResponseContentEncoding="ascii")

    streaming_body = response['Body']
    
    wtf = streaming_body.read().decode("ascii").split("\r\n")
    
    table_data = list(csv.reader(wtf))

    return table_data

# print(run('its-a-gas', 'Audi.csv'))
