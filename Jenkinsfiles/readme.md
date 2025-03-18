# 📂 Jenkinsfiles  

This folder contains Jenkins Pipeline scripts that automate the processes of building, testing, and deploying applications.  

## 📌 Contents  

### 🚀 creating_ami_pipeline  
🔹 Pulls a Docker image from the registry  
🔹 Builds an **AMI** using **Packer** and **Ansible**  

📄 **File:** [`creating_ami_pipeline`](Jenkinsfiles/creating_ami_pipeline)  

---
### 🐳 docker_run  
🔹 Automates pulling a Docker image  
🔹 Runs a container with specified configurations  
🔹 Executes a **Packer** build inside the container  

📄 **File:** [`docker_run`](Jenkinsfiles/docker_run)  

---

### 📦 docker_build_image  
🔹 Builds a Docker image from the **Dockerfile**  
🔹 Pushes the image to a Docker registry  

📄 **File:** [`docker_build_image`](Jenkinsfiles/docker_build_image)  

---

### 🌍 terraform_pipeline  
🔹 Defines a **CI/CD** pipeline using **Terraform**  
🔹 Manages AWS infrastructure provisioning  

📄 **File:** [`terraform_pipeline`](Jenkinsfiles/terraform_pipeline)  

---
