# 📂 ci_cd_pipelines  

This folder contains Jenkins Pipeline scripts that automate the processes of building, testing, and deploying applications.  

## 🚀 Creating AMI Pipeline  

This **Jenkins pipeline** automates the process of building an **Amazon Machine Image (AMI)** using **Packer** and **Ansible**.  
It runs inside a **Docker container**, ensuring a consistent environment across different builds.   
✔️ Pulls a pre-built **Docker image** from a registry  
✔️ Runs a **Docker container** with the required environment variables  
✔️ Initializes **Packer** and triggers the AMI build process  
✔️ Uses **Ansible** for configuration management  
✔️ Cleans up the workspace and removes the container after execution  

📄 **File:** [`creating_ami_pipeline`](Jenkinsfiles/creating_ami_pipeline)  

---
## 🐳 docker_run.sh  

This Bash script is used inside a **Jenkins pipeline** to automate the process of:  
✔️ Pulling a **Docker image** from a registry  
✔️ Running a **Docker container** with AWS credentials  
✔️ Executing a **Packer build** inside the container  
✔️ Debbuging (optional)  
✔️ Cleaning up after execution  


📄 **File:** [`docker_run`](Jenkinsfiles/docker_run)  

---

## 📦 docker_build_image  

This Jenkins pipeline automates the process of:  
✔️ Cloning a Git repository containing a **Dockerfile**  
✔️ Building a **Docker image** from the repository  
✔️ Logging into a **Docker registry**  
✔️ Pushing the built image to a **Docker registry**  

📄 **File:** [`docker_build_image`](Jenkinsfiles/docker_build_image)  

---

## 🌍 terraform_pipeline  
This Jenkins pipeline automates the process of:  
✔️ Cloning a **Terraform infrastructure repository**  
✔️ Retrieving the **latest AMI ID** dynamically from AWS  
✔️ Initializing and applying **Terraform configurations**  
✔️ Deploying or updating AWS infrastructure with Terraform  

📄 **File:** [`terraform_pipeline`](Jenkinsfiles/terraform_pipeline)  

---
