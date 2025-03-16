variable "region" {
  default = "ca-central-1"
}


/*data "aws_ami" "latest" {
  most_recent = true
  owners = ["self"]

  filter {
    name   = "name"
    values = ["ubuntu-*"] 
  }
}*/
variable "ami_id" {
  description = "The AMI ID to use for the launch template"
  type        = string
}
# Output the AMI ID
/*output "ami_id" {
  value = data.aws_ami.latest.id
}
*/
variable "instance_type" {
  default = "t2.medium"
}
