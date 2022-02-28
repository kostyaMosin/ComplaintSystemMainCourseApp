import boto3
from decouple import config
from fastapi import HTTPException


class S3Service:
    def __init__(self):
        self.key = config("AWS_ACCESS_KEY")
        self.secret = config("AWS_SECRET_KEY")
        self.endpoint_url = config("AWS_S3_ENDPOINT_URL")
        self.region = config("AWS_S3_REGION")
        self.s3 = boto3.client(
            "s3",
            aws_access_key_id=self.key,
            aws_secret_access_key=self.secret,
            endpoint_url=self.endpoint_url,
        )
        self.bucket = config("AWS_BUCKET_NAME")

    def upload_photo(self, path, key, ext):
        try:
            self.s3.upload_file(
                path,
                self.bucket,
                key,
                ExtraArgs={"ACL": "public-read", "ContentType": f"image/{ext}"},
            )
            return f"{self.endpoint_url}/{self.bucket}/{key}"
        except Exception as ex:
            raise HTTPException(500, "S3 is not available")
