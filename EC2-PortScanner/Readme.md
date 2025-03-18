# 🔎 EC2 Port Scanner

## 📖 Overview
This repository contains scripts that automate the process of identifying **AWS EC2 instances** and their associated **Security Groups (SGs)** that have a specified port open.

### 📜 Scripts:
- **`script.sh`** – Bash script for querying EC2 instances and security groups.
- **`instances.py`** – Python 3 script for performing the same operation programmatically.

## 🛠️ Requirements
- **AWS CLI** installed and configured with appropriate permissions.
- **Python 3** (if using `instances.py`).

## 🚀 Usage

### 🔹 Input Arguments:
1. **AWS Region** – The AWS region to query (e.g., `us-east-1`).
2. **Port Number** – The port to check (e.g., `443` for HTTPS).
3. **Instance State** – Specify whether to include only running instances (`1`) or both running and stopped instances (`0`).

### 🔹 Example Usage:
```sh
./script.sh us-east-1 443 1
```
### 🔹 Example Output:  
instance: i-0abcd12345 groups: sg-0a1b2c3d sg-0e4f5g6h  
instance: i-1bcde23456 groups: sg-0a1b2c3d
