import s3_operations as s3

"""
Getting list of buckets
"""
s3.listBuckets()
"""
Creating bucket with default region: Asia Pacific (Mumbai)
"""
# s3.createBucket("saurabh-sample2")
"""
Creating bucker with manually entering the region code
"""
# s3.createBucket("saurabh-sample3", "ap-south-1")
"""
Deleting Bucket
"""
# s3.deleteBucket("saurabh-sample2")
"""
Getting list of items in bucket
"""
# s3.listItemsBucket("saurabh-files")
"""
Uploding file in bucket, make sure the file name is correct and it exist in the same folder
"""
# s3.uploadFile("MyPic2.png", "saurabh-sample1")files
"""
Downloading file from bucket
"""
# s3.downloadFile("saurabh-files", "rootkey.csv", "rk.csv")
"""
Copy file from source bucket to destination bucket
"""
# s3.copyFile("saurabh-files", "saurabh-sample1", "MyPic2.png", "my.png")
"""
Delete file from bucket
"""
# s3.deleteFile("saurabh-sample1", "my.png")
"""
Deleting all files from bucket
"""
# s3.delete_all("saurabh-sample1")
