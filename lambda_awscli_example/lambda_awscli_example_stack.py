from aws_cdk import (
    Stack, Duration
)
from aws_cdk.aws_lambda import Runtime, LayerVersion, Function, Code
from constructs import Construct
from aws_cdk.lambda_layer_awscli import AwsCliLayer
from aws_cdk.asset_awscli_v2 import AwsCliAsset
import aws_cdk.aws_lambda as lambda_
import aws_cdk.aws_s3_assets as s3_assets
from aws_cdk import FileSystem

class LambdaAwscliExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        awscli = AwsCliAsset(self, "AwsCliCode")
        
        Function(self, 'MyFunction', 
            runtime=Runtime.PYTHON_3_11,
            handler='function.handler',
            timeout=Duration.seconds(30),
            code=Code.from_asset('lambda_awscli_example/lambda'),
            memory_size=1024,
            layers=[
                LayerVersion(self, "AwsCliLayer",code=lambda_.Code.from_bucket(awscli.bucket, awscli.s3_object_key)),
                LayerVersion.from_layer_version_arn(self, 'Powertools', f'arn:aws:lambda:{self.region}:017000801446:layer:AWSLambdaPowertoolsPythonV2:64')
            ]
        )