import base64
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # TODO implement
    dynamo_db = boto3.resource('dynamodb')
    table = dynamo_db.Table('stopTimeTable')
    
    decoded_record_data = [base64.b64decode(
        record['kinesis']['data']) for record in event['Records']]
    deserialized_data = [json.loads(decoded_record)
                         for decoded_record in decoded_record_data]
    
    with table.batch_writer() as batch_writer:
        for item in deserialized_data:
            
            stop_id = item['stop_id']
            trip_id = item['trip_id']
            arrival_time = item['arrival_time']
            departure_time = item['departure_time']
            stop_id = item['stop_id']
            stop_sequence = item['stop_sequence']
            shape_dist_traveled = item['shape_dist_traveled']
            stop_time_id = item['stop_time_id']
            
            logger.info('Sending record ' + stop_time_id+ ' to DynamoDB')
            
            batch_writer.put_item(
                Item={
                    'StopTimeID': stop_time_id,
                    'TripID': trip_id,
                    'ArrivalTime': arrival_time,
                    'DepartureTime': departure_time,
                    'StopID': stop_id,
                    'StopSequence': stop_sequence,
                    'ShapeDistTravel': shape_dist_traveled
                }
            )
            
            logger.info('Success!')
