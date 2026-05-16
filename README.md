# 🚀 Secure AWS Content Delivery Platform

Secure content access using **Amazon Cognito, API Gateway, AWS Lambda, JWT Authorization and Amazon S3 Pre-Signed URLs**.

This project demonstrates a **serverless AWS architecture** where private resources are never directly exposed. Users authenticate through Amazon Cognito and receive controlled, time-limited access to protected content stored in Amazon S3.

---

## 🌐 Project Overview

Traditional applications often expose APIs and storage resources directly, creating security risks:

❌ Public API exposure  
❌ No authentication checks  
❌ Direct S3 object access  
❌ Uncontrolled content sharing  

This project implements a secure access architecture using:

✅ Amazon Cognito Authentication  
✅ OAuth 2.0 Authorization Code Flow  
✅ JWT Protected APIs  
✅ AWS Lambda Serverless Backend  
✅ Private Amazon S3 Storage  
✅ Time-Limited Pre-Signed URLs  
✅ IAM Least Privilege Access  

---

## 🏗 Architecture Diagram

![Architecture](./architecture/secure_arc.png)

📘 Detailed architecture explanation:

👉 [Click here](./architecture/README.md)

---

## ⚡ Real-World Use Case

Consider a **Netflix-style secure video delivery platform**.

Without security:

- Anyone with a direct URL can access content
- Links can be shared indefinitely
- No access control exists

With this architecture:

- Users authenticate through Cognito
- JWT tokens validate every request
- S3 stays private
- Lambda generates temporary URLs
- Access automatically expires

---

## 🔄 End-to-End Workflow

```text
User
↓
Login using Amazon Cognito Hosted UI
↓
OAuth Authorization Code generated
↓
Authorization code sent to /token API
↓
Lambda exchanges code for JWT tokens
↓
JWT token used for protected API access
↓
API Gateway validates JWT
↓
Lambda generates Pre-Signed URL
↓
Private Amazon S3 Object
↓
Protected content access
```

---

## ☁ AWS Services Used

| Service | Purpose |
|---|---|
| Amazon Cognito | Authentication & User Management |
| API Gateway | Protected API Layer |
| AWS Lambda | Serverless Backend Logic |
| Amazon S3 | Private Content Storage |
| IAM | Least Privilege Access |
| JWT Authorizer | API Protection |
| CloudTrail | Audit Logs & Event Tracking |

---

## 🔐 Security Features

- OAuth 2.0 Authorization Code Flow
- JWT Token Validation
- Cognito Hosted UI Authentication
- API Gateway Route Protection
- Private S3 Bucket
- Block Public Access Enabled
- Temporary Pre-Signed URLs
- IAM Least Privilege
- Audit Logging Support
- Browser → Direct S3 Access Blocked

---

## 📸 Implementation Screenshots

Detailed implementation screenshots:

👉 [Click here](./screenshots/README.md)

Includes:

- Cognito setup
- Hosted UI login
- JWT flow
- API protection
- Private S3 validation
- Pre-signed URL generation
- Final secure content access

---

## 📘 Technical Documentation

Complete project documentation:

👉 [Click here](./documentation/README.md)

Documentation includes:

- Architecture walkthrough
- Authentication flow
- Security implementation
- Challenges & fixes
- IAM configuration
- Interview questions

---

## 🧠 Technical Notes

Additional implementation notes:

👉 [Click here](./docs/README.md)

---

## 🎬 Demo Videos

Project demonstrations:

👉 [Click here](./demo/README.md)

Includes:

- Full workflow demo
- AWS Console walkthrough
- Authentication flow
- Secure content access

---

## 📂 Project Structure

```text
secure-aws-content-delivery-platform/
│
├── architecture/
├── screenshots/
├── lambda-functions/
├── static-client/
├── iam-policies/
├── documentation/
├── docs/
├── demo/
│
└── README.md
```

---

## 🚧 Future Enhancements

- AWS WAF integration
- AWS Secrets Manager
- CloudFront CDN
- User groups and role-based access
- CloudWatch monitoring dashboards
- Automatic URL regeneration

---

## 🎯 Security Principle

Private resources should never be directly exposed.

Access should always happen through:

Authentication  
→ Authorization  
→ Controlled Temporary Access

---

## 👨‍💻 Author

**Adhithyan Sivaraman T**

GitHub:  :contentReference[oaicite:0]{index=0}

LinkedIn:  :contentReference[oaicite:1]{index=1}

---

⭐ If you found this project useful, consider giving it a star.
