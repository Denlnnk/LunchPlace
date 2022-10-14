import os
import json
import boto3
from boto3 import resource


class S3Connection(object):
    """ S3 connection class."""

    def __init__(self):
        self.resource = self._init_connection()
        self.bucket_name = os.getenv('RESTAURANT_BUCKET_NAME')

    @staticmethod
    def _init_connection():
        aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID')
        aws_secret_key_id = os.getenv('AWS_SECRET_KEY_ID')
        return resource('s3', "eu-central-1",
                        aws_access_key_id=aws_access_key_id,
                        aws_secret_access_key=aws_secret_key_id)

    def load_files_content(self):
        bucket = self.resource.Bucket(self.bucket_name)
        objects = bucket.objects.all()

        restaurant_info_list = []
        for my_bucket_object in objects:
            file_content = self.resource.Object(self.bucket_name, my_bucket_object.key).get()['Body'].read().decode(
                'utf-8')
            if file_content == '':
                continue

            json_content = json.loads(file_content)
            restaurant_info_list.append(json_content)

        return restaurant_info_list

    def upload_to_s3(self):
        s3 = self.resource
        files_root = os.path.abspath('static/restaurants/').replace('api/connections/', '')
        for files in os.listdir(files_root):
            with open(files, 'rb') as f:
                s3.Bucket(self.bucket_name).upload_fileobj(f, f'restaurant/{files}')

