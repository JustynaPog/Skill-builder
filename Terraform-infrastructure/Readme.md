# terraform_infrastructure

This repository can be used to create infrastructure in the AWS cloud, using Terraform.

Resources that will be created:
- Aplication Load Balancer (including: aws_lb, aws_lb_target_group, aws_lb_listener)
- Autoscaling Group (including:aws_autoscaling_group, aws_launch_template)
- Security Group (including:aws_security_group, aws_vpc_security_group_ingress_rule, aws_vpc_security_group_egress_rule)
