# Technical Documentation

This folder contains supporting implementation notes and technical explanations for the **Secure AWS Content Delivery Platform** project.

---

# Authentication Flow

1. User clicks **Login** from the HTML/JS demo page.
2. User is redirected to **Amazon Cognito Hosted UI**.
3. User authenticates successfully.
4. Cognito returns an **OAuth Authorization Code**.
5. Authorization code is sent to the **/token API endpoint**.
6. Token Exchange Lambda exchanges the authorization code.
7. JWT token is returned.
8. JWT token is used for protected API access.

---

# Secure Content Access Workflow

1. User sends JWT token to the protected API endpoint.
2. API Gateway validates the token using **JWT Authorizer**.
3. Only validated requests reach Lambda.
4. Lambda generates a **time-limited pre-signed URL**.
5. User accesses protected S3 content using temporary access.

**Direct browser access to S3 is blocked.**

---

# Security Principles

## Least Privilege Access
IAM permissions are restricted to only required actions.

## Private S3 Storage
Amazon S3 Block Public Access is enabled.

## JWT Authorization
Only authenticated users can invoke protected APIs.

## Temporary Access Pattern
Content access uses time-limited pre-signed URLs.

## Secure Architecture Principle

Private resources are never directly exposed.  
Access is granted only through authenticated APIs and temporary pre-signed URLs.

---

# Technical Highlights

- OAuth 2.0 Authorization Code Flow
- Amazon Cognito Hosted UI Authentication
- API Gateway with JWT Authorization
- Serverless Lambda backend
- Private Amazon S3 storage
- Temporary pre-signed URL generation
- CloudTrail audit support
- IAM least privilege access model

---

# Project Security Model

Browser → Cognito → JWT → Protected API → Lambda → Pre-Signed URL → Private S3 Object

This design ensures users never directly access private AWS resources.
