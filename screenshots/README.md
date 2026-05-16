# 📸 Implementation Screenshots

This folder contains implementation screenshots for the complete Secure AWS Content Delivery Platform workflow.

Authentication → JWT Validation → Protected APIs → Private S3 → Pre-Signed URL → Secure Content Access

---

# 🟢 Phase 1 — Cognito Authentication Setup

### 1. Cognito User Pool Configuration

![Cognito User Pool](./1-Cognito-User-Pool-Configuration.png)

---

### 2. App Client with OAuth Configuration

![App Client](./2-App-Client-with-OAuth-Configuration.png)

---

### 3. Cognito Hosted UI Login Page

![Hosted UI](./3-Cognito-Hosted-UI-Login-Page.png)

---

### 4. Authorization Code Received After Login

![Authorization Code](./4-Authorization-Code-Received-After-Login.png)

---

# 🟡 Phase 2 — Token Exchange Flow

### 5. Lambda Function for Authorization Code Exchange

![Lambda Token Exchange](./5-Lambda-Function-for-Authorization-Code-Exchange.png)

---

### 6. API Gateway Endpoint for Token Exchange

![API Gateway](./6-API-Gateway-Endpoint-for-Token-Exchange.png)

---

### 7. JWT Token Received After Exchange

![JWT Token](./7-JWT-Token-Received-After-Exchange.png)

---

# 🔵 Phase 3 — Secure API Protection

### 8. Secure API Endpoint Configuration

![Secure API](./8-Secure-API-Endpoint-Configuration.png)

---

### 9. Secure API Endpoint Configuration

![Secure API](./9-Secure-API-Endpoint-Configuration.png)

---

### 10. Unauthorized API Access Without Authentication

![Unauthorized Access](./10-Unauthorized-API-Access-Without-Authentication.png)

---

### 11. Successful API Access After Authentication

![Authenticated Access](./11-Successful-API-Access-After-Authentication.png)

---

# 🟣 Phase 4 — Secure S3 Protection

### 12. Private S3 Bucket with Block Public Access Enabled

![Private S3](./12-Private-S3-Bucket-with-Block-Public-Access-Enabled.png)

---

### 13. Direct S3 Object Access Denied (Security Validation)

![Denied](./13-Direct-S3-Object-Access-Denied-(Security-Validation).png)

---

### 14. Lambda Function to Generate Pre-Signed URL

![Lambda URL](./14-Lambda-Function-to-Generate-Pre-Signed-URL.png)

---

### 15. IAM Policy with s3:GetObject Permission

![IAM Policy](./15-IAM-Policy-with-s3GetObject-Permission.png)

---

### 16. Secure Endpoint for Generating Pre-Signed URL

![Protected Endpoint](./16-Secure-Endpoint-for-Generating-Pre-Signed-URL.png)

---

### 17. Protected S3 Access via JWT Authorizer

![JWT Protection](./17-Protected-S3-Access-via-JWT-Authorizer.png)

---

### 18. Pre-Signed URL Generated via Secure API

![Generated URL](./18-Pre-Signed-URL-Generated-via-Secure-API.png)

---

### 19. Secure Access to S3 Object Using Temporary URL

![Final Output](./19-Secure-Access-to-S3-Object-Using-Temporary-URL.png)

---

### Optional Screenshot

![Optional](./2-optional.png)

---

# ✅ Project Outcome

Successfully implemented:

- Amazon Cognito Authentication
- OAuth Authorization Code Flow
- JWT Authorization
- API Gateway Protected APIs
- AWS Lambda Backend
- Private S3 Architecture
- Temporary Secure Access using Pre-Signed URLs
- IAM Least Privilege Security

🚀 Production-style secure AWS architecture implementation
