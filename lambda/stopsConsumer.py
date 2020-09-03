import base64
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    dynamo_db = boto3.resource('dynamodb')
    table = dynamo_db.Table('stopsTable')
    
    decoded_record_data = [base64.b64decode(
        record['kinesis']['data']) for record in event['Records']]
    deserialized_data = [json.loads(decoded_record)
                         for decoded_record in decoded_record_data]
    
    with table.batch_writer() as batch_writer:
        for item in deserialized_data:
            
            stop_id = item['stop_id']
            stop_name = item['stop_name']
            zone_id = item['zone_id']
            stop_url = item['stop_url']
            location_type = item['location_type']
            parent_station = item['parent_station']
            
            logger.info('Sending record ' + stop_id + ' to DynamoDB')
            
            batch_writer.put_item(
                Item={
                    'StopID': stop_id,
                    'StopName': stop_name,
                    'ZoneID': zone_id,
                    'StopUrl': stop_url,
                    'LocationType': location_type,
                    'ParentStation': parent_station
                }
            )
            
            logger.info('Success!')
