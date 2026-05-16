# Project Demo

This folder contains demonstration resources for the **Secure AWS Content Delivery Platform** project.

The demo videos showcase both the complete application workflow and the AWS infrastructure implementation.

---

# Demo Video 1 — Complete Project Flow

This walkthrough demonstrates the complete end-to-end user flow:

- User login using Amazon Cognito Hosted UI
- OAuth authorization code flow
- JWT token generation
- Protected API access
- Pre-signed URL generation
- Accessing protected S3 content

▶️ **View Full Project Flow Demo:**  
[Click here to watch](https://drive.google.com/file/d/11YNzG_3BVVwWT3J0FHe-EdkXQx9-P2ax/view?usp=drive_link)

---

# Demo Video 2 — AWS Console Setup Walkthrough

This walkthrough demonstrates the AWS infrastructure and service configuration:

- Amazon Cognito setup
- API Gateway configuration
- Lambda functions
- JWT authorization
- IAM roles and permissions
- Private S3 bucket setup
- Overall architecture implementation

▶️ **View AWS Setup Walkthrough:**  
[Click here to watch](https://drive.google.com/file/d/1YDbCdfqv_u3VIlp0ellQbBIAMmgyAi89/view?usp=drive_link)

---

# Demo Summary

The project follows a secure architecture pattern:

User → Cognito Authentication → JWT Authorization → Protected API → Lambda → Pre-Signed URL → Private S3 Content

This ensures private resources are never directly exposed and access remains temporary and controlled.
