import json
import logging
import boto3
import csv
from io import BytesIO

logger = logging.getLogger()
logger.setLevel(logging.INFO)

 
def handler(event, context):
    
    logger.info('got event{}'.format(event))

    fileToProcess = event['Records'][0]['s3']['object']['key']
    logger.info(f'processing file [{fileToProcess}]')

    s3_resource = boto3.resource('s3')
    for bucket in s3_resource.buckets.all():
       print(bucket.name)

    bucket = s3_resource.Bucket('775297465882-secret-sauce-data')
    obj = bucket.Object(fileToProcess)
    response = obj.get()
    
    array = BytesIO(response['Body'].read())
    for line in array:
        print(line)
        line = line.decode("utf-8")
        entry = line.split(",")
        ticket_class = entry[5]
        travel_type = entry[6]

        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        results_table = dynamodb.Table('secret-sauce-results')
        
        if "coach" not in ticket_class and "domestic" in travel_type:
            employee = entry[1]
            logger.info(f'Violation Found [{employee}]')
            results_table.put_item(
                Item={
                    'uid': entry[1],
                    'employee': entry[0],
                    'violationCount': 1
                }
            )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
