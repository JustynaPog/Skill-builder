# 🌍 Terraform AWS Infrastructure

## 📖 Overview
This repository contains Terraform configurations for deploying infrastructure on **AWS Cloud**. The infrastructure includes **Application Load Balancer (ALB)**, **Autoscaling Group**, and **Security Groups**, ensuring a scalable and secure environment.

## 📌 Resources Created
The Terraform scripts will provision the following resources:

### 🔹 **Application Load Balancer (ALB)**
- `aws_lb` – Creates an ALB to distribute traffic.
- `aws_lb_target_group` – Defines a target group for routing requests.
- `aws_lb_listener` – Manages inbound connections to the ALB.

### 🔹 **Autoscaling Group**
- `aws_autoscaling_group` – Defines the autoscaling group for managing EC2 instances.
- `aws_launch_template` – Provides configuration for launching instances.

### 🔹 **Security Groups**
- `aws_security_group` – Manages security groups for controlling traffic.
- `aws_vpc_security_group_ingress_rule` – Defines inbound traffic rules.
- `aws_vpc_security_group_egress_rule` – Defines outbound traffic rules.
