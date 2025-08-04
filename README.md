# 🚀 DevOps Microservices Pipeline

A complete end-to-end DevOps demonstration project showcasing modern infrastructure automation, containerization, and CI/CD practices.

![Architecture](https://img.shields.io/badge/Architecture-Microservices-blue)
![Platform](https://img.shields.io/badge/Platform-AWS%20EKS-orange)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Jenkins-red)
![IaC](https://img.shields.io/badge/IaC-Terraform-purple)

## 📋 **Project Overview**

This project demonstrates a production-ready DevOps pipeline including:
- **Containerized Python Flask API** with health checks and proper logging
- **Kubernetes orchestration** with high availability and auto-scaling
- **Infrastructure as Code** using Terraform for AWS EKS deployment
- **Automated CI/CD pipeline** with Jenkins for continuous deployment
- **Enterprise security practices** with proper IAM roles and network segmentation

## 🏗️ **Architecture**

┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│   GitHub    │───▶│   Jenkins    │───▶│   Docker    │───▶│ Kubernetes   │
│ Source Code │    │   CI/CD      │    │ Container   │    │   AWS EKS    │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
│                    │                   │
▼                    ▼                   ▼
┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│  Automated   │    │   Image     │    │ Load Balanced│
│   Testing    │    │  Registry   │    │   Service    │
└──────────────┘    └─────────────┘    └──────────────┘

## 🛠️ **Technology Stack**

### **Application Layer**
- **Python 3.9** - Backend application development
- **Flask** - RESTful API framework with JSON responses
- **SQLite** - Lightweight database for user management
- **Gunicorn** - Production WSGI server

### **Containerization**
- **Docker** - Application containerization
- **Multi-stage builds** - Optimized container images
- **Health checks** - Container monitoring and recovery

### **Orchestration**  
- **Kubernetes** - Container orchestration and scaling
- **AWS EKS** - Managed Kubernetes service
- **kubectl** - Cluster management and deployment

### **Infrastructure as Code**
- **Terraform** - Infrastructure provisioning and management
- **AWS VPC** - Network isolation and security
- **IAM Roles** - Least privilege access control
- **Security Groups** - Network-level firewall rules

### **CI/CD Pipeline**
- **Jenkins** - Automation server and pipeline orchestration
- **Pipeline as Code** - Jenkinsfile-defined workflows
- **Automated testing** - Health checks and validation
- **Rolling deployments** - Zero-downtime updates

### **Cloud Platform**
- **Amazon Web Services (AWS)** - Cloud infrastructure
- **EKS** - Managed Kubernetes control plane
- **EC2** - Scalable compute instances
- **VPC** - Virtual private cloud networking

## 📁 **Project Structure**

devops-microservices-pipeline/
├── app/                        # Python Flask Application
│   ├── app.py                 # Main application with REST endpoints
│   ├── requirements.txt       # Python dependencies
│   ├── Dockerfile            # Container build instructions
│   └── tests/                # Automated test suite
├── k8s/                       # Kubernetes Manifests
│   ├── deployment.yaml       # Application deployment configuration
│   ├── service.yaml          # Service and load balancer setup
│   └── configmap.yaml        # Configuration management
├── terraform/                 # Infrastructure as Code
│   ├── main.tf               # Primary Terraform configuration
│   ├── variables.tf          # Input variables and defaults
│   ├── outputs.tf            # Infrastructure outputs
│   └── kubeconfig.tpl        # Kubectl configuration template
├── scripts/                   # Automation Scripts
│   ├── terraform-deploy.sh   # Infrastructure deployment automation
│   ├── terraform-destroy.sh  # Resource cleanup automation
│   └── build.sh              # Application build automation
├── jenkins/                   # CI/CD Pipeline
│   └── Jenkinsfile           # Pipeline as Code definition
└── monitoring/                # Observability Configuration
└── prometheus-config.yml  # Metrics collection setup

## 🚀 **Quick Start**

### **Prerequisites**
- Docker Desktop with Kubernetes enabled
- AWS CLI configured with appropriate permissions
- Terraform >= 1.0
- kubectl CLI tool
- Python 3.9+ (for local development)

### **Local Development**
```bash
# Clone the repository
git clone https://github.com/gkrainis/devops-microservices-pipeline.git
cd devops-microservices-pipeline

# Set up Python virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r app/requirements.txt

# Run application locally
python app/app.py

# Test endpoints
curl http://localhost:5000/health
curl http://localhost:5000/users
