#!/usr/bin/env python3

import boto3
import os
from os.path import join,dirname
from dotenv import load_dotenv

load_dotenv(join(dirname(__file__),'..','..','.env'))

S3_BUCKET = os.getenv('AWS_BUCKET')
AWS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION= os.getenv('AWS_REGION')

'''
s3 = boto3.resource('s3',aws_access_key_id = AWS_KEY, aws_secret_access_key = AWS_SECRET, region_name = AWS_REGION)

def list_all_bucket_contents(resource, bucket_name):
    bucket = resource.Bucket(bucket_name)
    for obj in bucket.objects.all():
        print(obj.key)
'''

s3 = boto3.client('s3',aws_access_key_id = AWS_KEY, aws_secret_access_key = AWS_SECRET, region_name = AWS_REGION)
def list_all_bucket_contents(client, bucket_name):
    paginator = client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name)
    # First, just skip any empty directories, ending with a /
    # Also, just skip thumb/med/large dirs
    # Create a dict that has a key of the s3 "dir" 
    # Check if dir doesn't exist, if not, add key with empty list
    # append file name to list
    dirstructure = dict()
    for page in pages:
        for obj in page['Contents']:
            keyname = obj['Key']
            if keyname.endswith('/'):
                continue
            pathlist = keyname.rsplit('/',1)
            filename = pathlist[-1]
            dirname = None
            #If we are at the root (should just be error.html, maybe more), no split will happen and no dir will exist in the list
            if len(pathlist) == 2:
                dirname = pathlist[0]

            if dirname is not None:
                if dirname.rsplit('/',1)[-1] not in ['large', 'medium', 'thumbs']:
                    if dirname not in dirstructure:
                        dirstructure[dirname] = []
                    dirstructure[dirname].append(filename)
    return dirstructure

if __name__ == '__main__':
    structure = list_all_bucket_contents(s3, S3_BUCKET)
    print(structure)