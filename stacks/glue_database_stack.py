from aws_cdk import (
    Stack,
    aws_glue as glue,
)
from constructs import Construct

class GlueDatabaseStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Glue Catalog Database
        self.database = glue.CfnDatabase(
            self, "FinanceDatabase",
            catalog_id=self.account,
            database_input=glue.CfnDatabase.DatabaseInputProperty(
                name="finance_db"
            )
        )
