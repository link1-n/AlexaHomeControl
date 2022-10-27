#!/usr/bin/env python

import boto3
import time
import os

access_key = "########"
access_secret = "################"
region = "eu-west-1"
queue_url = "https://sqs.eu-west-1.amazonaws.com/440946986705/RPiAlexa"

def pop_message(client, url):
    response = client.receive_message(QueueUrl = url, MaxNumberOfMessages = 10)

    #last message posted becomes messages
    message = response['Messages'][0]['Body']
    receipt = response['Messages'][0]['ReceiptHandle']
    client.delete_message(QueueUrl = url, ReceiptHandle = receipt)
    return message

client = boto3.client('sqs', aws_access_key_id = access_key, aws_secret_access_key = access_secret, region_name = region)
                    
waittime = 20
client.set_queue_attributes(QueueUrl = queue_url, Attributes = {'ReceiveMessageWaitTimeSeconds': str(waittime)})

time_start = time.time()

while (time.time() - time_start < 60):
    print("Checking...")
    try:
        message = pop_message(client, queue_url)
        print(message)
        if message == "on":
            os.system("echo 'on 0.0.0.0' | cec-client -s -d 1")
        elif message == "off":
            os.system("echo 'standby 0.0.0.0' | cec-client -s -d 1")
        elif message == "hd1":
            os.system("echo 'tx 4F:82:10:00' | cec-client -s -d 1")
        elif message == "hd2":
            os.system("echo 'tx 4F:82:20:00' | cec-client -s -d 1")
        elif message == "hd3":
            os.system("echo 'tx 4F:82:30:00' | cec-client -s -d 1")
        elif message == "hd4":
            os.system("echo 'tx 4F:82:40:00' | cec-client -s -d 1")
    except:
        pass

