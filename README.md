
# MLOps Kubernetes Project

This repository contains a comprehensive MLOps project that demonstrates how to train, register, and deploy a machine learning model on Kubernetes.

## Table of Contents
- [Overview](#overview)
- [Project Architecture](#project-architecture)
- [Key Features](#key-features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Future Work](#future-work)

## Overview
This project serves as a practical demonstration of MLOps best practices, including infrastructure as code (IaC), automated model training, and production deployment. The project uses a Logistic Regression model trained on the Iris dataset, which is then deployed as a web service on a Minikube cluster.

## Project Architecture
The project is architected to follow a standard MLOps workflow:
1.  **Infrastructure as Code (IaC):** Terraform is used to provision the required Kubernetes resources.
2.  **ML Pipeline:** A Kubeflow pipeline trains and evaluates the model, achieving an accuracy of 97.33%.
3.  **Model Registry:** The trained model is versioned and registered with MLflow, with automated stage transitions from Staging to Production.
4.  **Production Deployment:** The model is containerized using Docker and deployed on a Minikube cluster with three active replicas for high availability.
5.  **Load Balancing:** Nginx is configured as a reverse proxy to manage traffic and ensure reliable access to the model service.

## Key Features
- **Automated Infrastructure:** The Kubernetes environment is automatically configured using Terraform.
- **ML Pipeline:** A Kubeflow pipeline is used to train and evaluate the model, achieving 97.33% accuracy.
- **Model Registry:** The trained model is registered and tracked using MLflow, with automated stage transitions from Staging to Production.
- **Production Deployment:** The model is deployed on a Minikube cluster with three active replicas for high availability.
- **Load Balancing:** Nginx is used as a reverse proxy to expose the model service and ensure reliable access.

## Technologies Used
- **Terraform:** For automating infrastructure setup.
- **Kubeflow:** For building and managing the ML pipeline.
- **MLflow:** For model tracking and registry.
- **Kubernetes:** For container orchestration and deployment.
- **Docker:** For containerizing the application.
- **Python:** For ML model development.

## Getting Started

### Prerequisites
- Docker
- Minikube
- Terraform
- Kubectl

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AwemerShafiq2025/k8s-mlops-project.git
    cd k8s-mlops-project
    ```
2.  **Set up the infrastructure:**
    ```bash
    cd infra
    terraform init
    terraform apply
    ```
3.  **Run the ML pipeline:**
    ```bash
    python ml_pipeline.py
    ```

## Project Structure
```
.
├── Dockerfile
├── README.md
├── infra
│   ├── .terraform.lock.hcl
│   ├── main.tf
│   ├── providers.tf
│   ├── terraform.tfstate
│   ├── terraform.tfstate.backup
│   └── variables.tf
├── iris_pipeline.yaml
├── ml_pipeline.py
├── mlflow_register.py
├── model-service.yaml
├── model-serving.yaml
└── student_info.txt
```

## Future Work
- Integrate a CI/CD pipeline for automated testing and deployment.
- Implement more advanced model monitoring and logging.
- Explore more complex datasets and models.
