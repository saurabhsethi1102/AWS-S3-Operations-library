import os
import json
import boto3
import botocore
from botocore.exceptions import ClientError

"""
Getting the list of Buckets
"""
def listBuckets():
    try:
        s3 = boto3.client('s3')
        response = s3.list_buckets()
        print('List of Buckets:')
        for bucket in response['Buckets']:
            print(f'{bucket["Name"]}')
    except ClientError as e:
        print(e)

"""
Creating a new Bucket
"""
def createBucket(bucket_name, region="ap-south-1"):
    try:
        if region is None:
            s3 = boto3.client('s3')
            s3.create_bucket(Bucket=bucket_name)
        else:
            s3 = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
        print ("Bucket created")
    except ClientError as e:
        print(e)


"""
Delete bucket
"""
def deleteBucket(bucket_name):
    try:
        flag=0
        s3 = boto3.resource('s3')
        bucket=s3.Bucket(bucket_name)
        for key in bucket.objects.all():
            if key:
                flag=1
                break
            else:
                flag=0
        if flag==1:
            print('Bucket is not empty, Would you like to delete now also?\n1.Yes\n2.No')
            ch=int(input('Enter 1 or 2'))
            if ch==1:
                for key in bucket.objects.all():
                    key.delete()
            elif ch==0:
                exit()
        bucket.delete()
        print('Bucket Deleted')
    except ClientError as e:
        print(e)


"""
Getting List of Items in a bucket
"""
def listItemsBucket(bucket_name):
    try:
        s3=boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        print('List of Items in', bucket_name)
        for items in bucket.objects.all():
            print(items.key)
    except ClientError as e:
        print(e)


"""
Uploading file to Bucket
"""
def uploadFile(file_name, bucket_name, object_name=None):
    s3=boto3.client('s3')
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print("File Uploaded")
    except ClientError as e:
        print(e)

"""
Downlodind file from Bucket
"""
def downloadFile(bucket_name, object_name, file_name):
    try:
        s3=boto3.resource('s3')
        s3.meta.client.download_file(bucket_name, object_name, file_name)
        print('File Downloaded Successfully')
    except ClientError as e:
        print(e)

"""
Copy a file from one bucket to another
"""
def copyFile(source_bucket_name, dest_bucket_name, source_file, dest_file):
    try:
        s3=boto3.resource('s3')
        s3.meta.client.download_file(source_bucket_name, source_file, source_file)
        s3.meta.client.upload_file(source_file, dest_bucket_name, dest_file)
        os.remove(source_file)
        print('File copied from', source_bucket_name, 'to', dest_bucket_name)
    except ClientError as e:
        print(e)

"""
Delete file from bucket
"""
def deleteFile(bucket_name, file_name):
    try:
        s3=boto3.resource('s3')
        obj=s3.Object(bucket_name, file_name)
        obj.delete()
        print('File Deleted')
    except ClientError as e:
        print(e)

"""
Deleting all files from bucket
"""
def delete_all(bucket_name):
    try:
        s3=boto3.resource('s3')
        bucket=s3.Bucket(bucket_name)
        for key in bucket.objects.all():
            key.delete()
        print("All Files deleted")
    except ClientError as e:
        print(e)

"""
Getting bucket location
"""
def get_bucket_location(bucket_name):
    try:
        s3=boto3.client('s3')
        response = s3.get_bucket_location(
            Bucket=bucket_name
        )
        print (response['LocationConstraint'])
    except ClientError as e:
        print(e)

"""
Getting bucket Access Control List
"""
def get_bucket_acl(bucket_name):
    try:
        s3 = boto3.client('s3')
        result = s3.get_bucket_acl(Bucket=bucket_name)
        print(result)
    except ClientError as e:
        print(e)

# """
# Getting bucket policy
# """
# def get_bucket_policy(bucket_name):
#     try:
#         s3=boto3.client('s3')
#         result = s3.get_bucket_policy(Bucket=bucket_name)
#         print(result)
#     except ClientError as e:
#         print(e)

# """
# Setting bucket policy
# """
# def set_bucket_policy(bucket_name):
#     try:
#         s3=boto3.client('s3')
#         print("Please enter the followting info to set bucket policy")
#         version=input('Version: ')
#         sid=input('Sid: ')
#         effect=input('Effect: ')
#         principal=input('Principal: ')
#         action=input('Action: ')
#         bucket_policy={
#             'Version': version,
#             'Statement': [{
#                 'Sid': sid,
#                 'Effect': effect,
#                 'Principal': principal,
#                 'Action': [action],
#                 'Resource' : "arn:aws:s3:::%s/*" %bucket_name
#             }]
#         }
#         bucket_policy=json.dumps(bucket_policy)
#         s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
#         print("Bucket Policy set successfull")
#     except ClientError as e:
#         print(e)

"""
Getting object as torrent
"""
def get_file_as_torrent(bucket_name, file_name):
    s3=boto3.client('s3')
    response=s3.get_object_torrent(
        Bucket = bucket_name,
        Key = file_name,
        RequestPayer = 'requester'
    )
    print (response)

"""
Getting object url
"""
def get_file_url(bucket_name, file_name):
    s3 = boto3.client('s3')
    location = s3.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    url = "https://s3-%s.amazonaws.com/%s/%s" % (location, bucket_name, file_name)
    print(url)