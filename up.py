import logging

import boto3
from boto3.s3.transfer import TransferConfig
from botocore.exceptions import ClientError

from progress import ProgressPercentage

# Upload the file
s3_client = boto3.client('s3')

# Create SQS client
sqs_client = boto3.client('sqs')


def upload(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    config = TransferConfig(multipart_threshold=1024 * 5, max_concurrency=10, multipart_chunksize=1024 * 5,
                            use_threads=True)
    extra = {'ContentType': 'text/plain'}

    try:
        # response = s3_client.upload_file(file_name, bucket, object_name)
        response = s3_client.upload_file(file_name, bucket, object_name, Callback=ProgressPercentage(file_name))
    except ClientError as e:
        logging.error(e)
        return False
    return True


def notify(file):
    queue_url = 'https://sqs.us-east-2.amazonaws.com/384989233858/spvNotification/'
    # tls
    # "https://sqs.us-east-2.amazonaws.com/384989233858/spvNotification"
    # Send message to SQS queue
    response = sqs_client.send_message(
        QueueUrl=queue_url,
        DelaySeconds=1,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': "nuevo archivo"
            },
            'Author': {
                'DataType': 'String',
                'StringValue': 'nosotros'
            },
            'WeeksOn': {
                'DataType': 'Number',
                'StringValue': '6'
            }
        },
        MessageBody=(
            file
        )
    )
    print("\n")
    print(response)


if "__main__" == __name__:
    file_name = "Resumen01-005.txt"
    if upload(file_name, "spvresumen"):
        notify(file_name)
