import base64
import json
import boto3
import csv
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    dynamo_db = boto3.resource('dynamodb')
    table = dynamo_db.Table('routesTable')
    
    decoded_record_data = [base64.b64decode(
        record['kinesis']['data']) for record in event['Records']]
    deserialized_data = [json.loads(decoded_record)
                         for decoded_record in decoded_record_data]
    
    with table.batch_writer() as batch_writer:
        for item in deserialized_data:
            
            route_id = item['route_id']
            route_short_name = item['route_short_name']
            route_long_name = item['route_long_name']
            route_type = item['route_type']
            route_url = item['route_url']
            
            logger.info('Sending record ' + route_id + ' to DynamoDB')
            
            batch_writer.put_item(
                Item={
                    'RouteID': route_id,
                    'RouteShortName': route_short_name,
                    'RouteLongName': route_long_name,
                    'RouteType': route_type,
                    'RouteUrl': route_url
                }
            )
            
            logger.info('Success!')
            
