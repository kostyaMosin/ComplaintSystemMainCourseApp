import boto3
from decouple import config


class SESService:
    def __init__(self):
        self.key = config("AWS_ACCESS_KEY")
        self.secret = config("AWS_SECRET_KEY")
        self.endpoint_url = config("AWS_SES_ENDPOINT_URL")
        self.region = config("AWS_SES_REGION")
        self.ses = boto3.client(
            "ses",
            region_name=self.region,
            aws_access_key_id=self.key,
            aws_secret_access_key=self.secret,
            endpoint_url=self.endpoint_url,
        )

    def send_mail(self, subject, to_addresses, text_data):
        body = {"Text": {"Data": text_data, "Charset": "UTF-8"}}

        self.ses.send_email(Source="mkv150293@gmail.com",
                            Destination={"ToAddresses": to_addresses,
                                         "CcAddresses": [],
                                         "BccAddresses": []},
                            Message={"Subject": {"Data": subject, "Charset": "UTF-8"},
                                     "Body": body}
                            )
