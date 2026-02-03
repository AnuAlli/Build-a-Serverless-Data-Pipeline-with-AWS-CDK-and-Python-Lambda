#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.lambda_stack import LambdaStack
from stacks.glue_database_stack import GlueDatabaseStack
from stacks.glue_pipeline_stack import GluePipelineStack

app = cdk.App()

# Define Stacks
db_stack = GlueDatabaseStack(app, "GlueDatabaseStack")
lambda_stack = LambdaStack(app, "LambdaStack")
pipeline_stack = GluePipelineStack(app, "GluePipelineStack")

app.synth()
