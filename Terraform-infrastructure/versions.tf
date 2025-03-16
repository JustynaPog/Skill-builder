terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">=4.67.0"
    } 
  }
  required_version = ">= 1.9.2"


  backend "s3" {
    bucket = "terraform-tfstate-jenkins"
    key = "terraform/terraform.tfstate"
    region = "ca-central-1"

  }
}
