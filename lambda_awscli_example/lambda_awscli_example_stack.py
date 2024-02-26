from aws_cdk import (
    Stack, Duration
)
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from aws_cdk.aws_lambda import Runtime, LayerVersion
from constructs import Construct
from aws_cdk.lambda_layer_awscli import AwsCliLayer

class LambdaAwscliExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        
        func = PythonFunction(self, 'MyFunction', 
            runtime=Runtime.PYTHON_3_11,
            handler='handler',
            timeout=Duration.seconds(30),
            entry='lambda_awscli_example/lambda',
            index='function.py',
            layers=[
                AwsCliLayer(self, 'AwsCliLayer'), 
                LayerVersion.from_layer_version_arn(self, 'Powertools', 'arn:aws:lambda:eu-west-1:017000801446:layer:AWSLambdaPowertoolsPythonV2:64')
            ]
        )