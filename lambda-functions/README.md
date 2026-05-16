# Lambda Functions

This folder contains Lambda functions used in the serverless backend layer.

## 1. TokenExchange.py
Purpose:
- Receives OAuth authorization code
- Exchanges code with Amazon Cognito
- Returns JWT access token

## 2. GeneratePreSignedURL.py
Purpose:
- Validates request
- Generates time-limited S3 pre-signed URLs
- Provides temporary access to private content

## 3. Authorizer / helper Lambda
Purpose:
- Supports authentication flow and secure API interaction

Security Notes:
- Uses IAM least privilege
- Works with JWT protected APIs
- No direct S3 exposure
