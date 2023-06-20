import boto3

# AWS access keys (These keys are fake, this won't work so fuck off! :) )
access_key = 'AKIA6GW4DKRWSGKUJVYQ'
secret_key = '1wictaRd/cORSmrar2CKEparsaMTU5SFGmBqKPhv'

# S3 bucket name and file path
bucket_name = 'your_bucket_name'
file_path = 'path_to_your_file'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Upload the file to S3
try:
    s3.upload_file(file_path, bucket_name, file_path)
    print("File uploaded successfully.")
except Exception as e:
    print("Error uploading file: ", str(e))
