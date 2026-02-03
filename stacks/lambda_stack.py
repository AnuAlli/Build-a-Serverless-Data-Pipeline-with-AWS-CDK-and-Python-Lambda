from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_s3 as s3,
)
from constructs import Construct

class LambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Bucket for raw data
        bucket = s3.Bucket(self, "FinanceRawDataBucket")

        # Lambda to fetch Alpha Vantage data
        fetch_function = _lambda.Function(
            self, "FetchAlphaVantageData",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="fetch_data.handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                "BUCKET_NAME": bucket.bucket_name,
                "API_KEY": "YOUR_ALPHA_VANTAGE_KEY"
            }
        )
        
        bucket.grant_write(fetch_function)
