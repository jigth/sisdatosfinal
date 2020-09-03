import base64
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    dynamo_db = boto3.resource('dynamodb')
    table = dynamo_db.Table('trainTable')
    
    decoded_record_data = [base64.b64decode(
        record['kinesis']['data']) for record in event['Records']]
    deserialized_data = [json.loads(decoded_record)
                         for decoded_record in decoded_record_data]
    
    with table.batch_writer() as batch_writer:
        for item in deserialized_data:

            route_id = item['route_id']
            service_id = item['service_id'][:10].replace("_","-")
            trip_id = item['trip_id']
            trip_headsign = item['trip_headsign']
            direction_id = item['direction_id']
            
            logger.info('Sending record ' + trip_id + ' to DynamoDB')
            
            batch_writer.put_item(
                Item={
                    'TripID': trip_id,
                    'RouteID': route_id,
                    'Date': service_id,
                    'TripHeadsign': trip_headsign,
                    'DirectionID': direction_id
                }
            )
            
            logger.info('Success!')
