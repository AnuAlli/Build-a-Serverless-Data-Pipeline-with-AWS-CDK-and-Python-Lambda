# AWS Serverless Finance Data Pipeline

## Overview
A serverless pipeline using AWS CDK to analyze finance data from 3 sources:
1. **Historical Stock Data:** Amazon Aurora
2. **Historical FOREX Data:** S3 (JSON)
3. **Intraday Stock Data:** Alpha Vantage API

## Tech Stack
- **Language:** Python
- **IaC:** AWS CDK
- **Compute:** AWS Lambda, AWS Glue
- **Storage:** Amazon S3, Amazon Aurora
- **Analysis:** Amazon Athena, Amazon QuickSight

## Architecture
- **Lambda Stack:** Handles API data fetching
- **Glue Database Stack:** Defines schema and Catalog
- **Glue Pipeline Stack:** ETL jobs for transformation

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Deploy: `cdk deploy --all`
