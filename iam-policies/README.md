# IAM Policies

This folder contains IAM policies used in the project.

Security principles followed:

- Least privilege access
- Lambda allowed only required S3 actions
- API Gateway invokes only required functions
- S3 access restricted to authorized components

Example permissions:

- s3:GetObject
- lambda:InvokeFunction
- logs:CreateLogGroup
- logs:CreateLogStream
