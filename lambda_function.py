import json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

 
def handler(event, context):
    
    logger.info('got event{}'.format(event))

    s3_resource = boto3.resource('s3')
    for bucket in s3_resource.buckets.all():
       print(bucket.name)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
