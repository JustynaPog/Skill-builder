# Jenkinsfiles

## creating_ami_pipeline
This script pulls docker image from registry and builds ami using packer and ansible (from repo).

## docker_run
This script automates the process of pulling a Docker image, running a container with specified configurations, and executing a Packer build inside the container.

## docker_build_image
This script builds docker image from Dockerfile in repo and pushes it to docker registry.

## terraform pipeline
This Jenkins pipeline script defines a continuous integration/continuous deployment (CI/CD) process that uses Terraform to manage infrastructure on AWS.

