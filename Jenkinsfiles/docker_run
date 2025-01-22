#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login docker.io -u "justynaph" --password-stdin
docker pull docker.io/justynaph/packer-ansible-image:latest
#docker run -dit --name packer-container1 -v /var/lib/jenkins/workspace:/workspace docker.io/justynaph/packer-ansible-image:latest
docker run -dit --name packer-container1 \
  -v /var/lib/jenkins/workspace:/workspace \
  -e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
  -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
  docker.io/justynaph/packer-ansible-image:latest

### packer build inside container ###

docker exec -i packer-container1 packer init /workspace/docker/packer/aws-ubuntu.pkr.hcl
docker exec -i packer-container1 packer build /workspace/docker/packer/aws-ubuntu.pkr.hcl

#### debugging ####
   #docker exec -i packer-container1 sh -c "export PACKER_LOG=1 && export PACKER_LOG_PATH=/workspace/packer.log && packer build /workspace/docker/packer/aws-ubuntu.pkr.hcl"
   #docker exec -i packer-container1 cat /workspace/packer.log

docker rm -f packer-container1 || true
