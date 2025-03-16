# 🚀 AWS EC2 Security Group Monitor  

This repository contains an AWS Lambda function that monitors open ports in EC2 Security Groups and sends email notifications if any instances have publicly accessible ports.  

## 📌 Features  

- ✅ Scans all **running EC2 instances** and their associated **Security Groups**  
- ✅ Checks for **open ports (0.0.0.0/0)** based on instance tags or default values  
- ✅ Sends **email alerts** using AWS Simple Email Service (SES) to predefined recipients  
- ✅ Supports **customizable notifications** through instance tags (`OpenPorts`, `AlertEmails`)  

## 🛠 How It Works  

1️⃣ **Retrieves all running EC2 instances** and their associated Security Groups  
2️⃣ **Extracts open ports** from instance tags or uses default ports (`22`, `80`)  
3️⃣ **Scans Security Groups** for rules that expose ports to the public (`0.0.0.0/0`)  
4️⃣ **Matches instances with open ports** and gathers notification email addresses  
5️⃣ **Sends a consolidated alert email** to all listed recipients via AWS SES  

## ⚙️ Configuration  

To use this function, configure the following environment variables:  

| Variable         | Description                                      | Default Value             |
|-----------------|--------------------------------------------------|---------------------------|
| `SES_SENDER_EMAIL` | Sender email address for AWS SES notifications | `noreply@example.com` |

Ensure that:  
✔️ The sender email/domain is verified in AWS SES  
✔️ The IAM role for Lambda has the necessary permissions (`ses:SendEmail`, `ec2:DescribeInstances`, `ec2:DescribeSecurityGroups`)  

## 📨 Example Email Alert  
Subject: AWS Security Alert: Open Ports on EC2 Instances  
The following EC2 instances have open ports accessible to the world (0.0.0.0/0):  
🔹Instance ID: i-1234567890abcdef  
🔹Open Ports: 22, 80  
🔹Security Groups: sg-abcdefgh

