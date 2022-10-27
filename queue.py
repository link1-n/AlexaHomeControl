import boto3

access_key = "AKIAWNKT5B3IS54CWBEN"
access_secret = "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"
region = "eu-west-1"
queue_url = "https://sqs.eu-west-1.amazonaws.com/440946986705/RPiAlexa"

client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)

client.send_message(QueueUrl = queue_url, MessageBody = "bruh")

response = client.receive_message(QueueUrl = queue_url, MaxNumberOfMessages = 10)

print(response)

