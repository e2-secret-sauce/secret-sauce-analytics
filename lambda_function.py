import json
import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

 
def handler(event, context):
    
    logger.info('got event{}'.format(event))

    fileToProcess = event['Records'][0]['s3']['object']['key']
    logger.info(f'processing file [{fileToProcess}]')

    s3_resource = boto3.resource('s3')
    for bucket in s3_resource.buckets.all():
       print(bucket.name)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
