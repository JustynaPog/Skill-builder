resource "aws_launch_template" "web" {
  name_prefix   = "web-server"
  image_id      = var.ami_id
  instance_type = var.instance_type
  # key_name      = var.key_name

  network_interfaces {
    security_groups             = [aws_security_group.web_sg.id]
    associate_public_ip_address = true
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_autoscaling_group" "web_asg" {
  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }

  vpc_zone_identifier = ["subnet-xxxx"]

  max_size = 2
  min_size = 1

  target_group_arns = [aws_lb_target_group.web_tg.arn]

  health_check_type         = "ELB"
  health_check_grace_period = 300

  tag {
    key                 = "Name"
    value               = "WebServerASG"
    propagate_at_launch = true
  }
}
