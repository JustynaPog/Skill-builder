# Repository Overview

📌 This repository contains a **Dockerfile** that builds a **lightweight Ubuntu 24.04-based container** with **Ansible** and **Packer** pre-installed.  
Perfect for DevOps tasks, infrastructure automation, and CI/CD environments. 

## 🚀 Features  
✔ Based on the latest Ubuntu 24.04  
✔ Pre-installed **Ansible** for configuration management  
✔ Includes **Packer** for automated machine image creation  
✔ **Non-root user (`packer`)** with sudo access  

## 🛠 Prerequisites  
Make sure you have **Docker installed** on your system:  
🔗 [Docker Installation Guide](https://docs.docker.com/get-docker/)  

## 🏗 Building the Docker Image
To build the Docker image locally, follow these steps:  

1️⃣ **Clone this repositor**:  
```sh
git clone <repository-url>
cd <repository-directory>
```
2️⃣ **Build the Docker image**:
```sh
docker build -t ubuntu-ansible-packer
```
🔹 This will create a new Docker image named `ubuntu-ansible-packer` based on **Ubuntu 24.04**, with **Ansible** and **Packer** pre-installed.

## ▶ Running the Container  
Once the image is built, you can run a container using different modes:  

🔹 **Interactive Mode (Recommended for testing)**  
To start a container and get an interactive shell:  
```sh
docker run -it ubuntu-ansible-packer
```
🔹 **Detached Mode (Running in the background)**  
To run the container in the background:  
```sh
docker run -d --name ansible-packer-container ubuntu-ansible-packer
```
You can later attach to the running container with:  
```sh
docker exec -it ansible-packer-container sh
```

## 🧹 Cleaning Up (Removing the Container)  
To stop and remove the container:  
```sh
docker stop ansible-packer-container  
docker rm ansible-packer-container
```
## 🔥 Use Cases
This container is useful for:
✔ Testing and developing Ansible playbooks 📝  
✔ Automating image creation workflows with Packer 📦  
✔ Creating a portable DevOps/CI/CD environment 🚀

