# CI/CD Pipeline for a Python Flask Application

This repository is a hands-on demonstration of a complete CI/CD pipeline for a Python (Flask) web application. The project showcases skills in containerization with Docker, automation with GitHub Actions, and configuration management with Ansible.

[![CI-CD Pipeline Status](https://github.com/Pavel-Molchan/home-labe/actions/workflows/main.yml/badge.svg)](https://github.com/Pavel-Molchan/home-labe/actions/workflows/main.yml)

## 🚀 Features

- **Containerization**: Optimized multi-stage `Dockerfile` for a small and secure production image.
- **Local Development**: `docker-compose.yml` for easy one-command setup of the application and a PostgreSQL database.
- **Continuous Integration (CI)**:
  - Code linting with **flake8** to ensure code quality.
  - Unit testing with **pytest** to verify application logic.
- **Continuous Delivery (CD)**:
  - Automated builds of Docker images using **GitHub Actions**.
  - Automatic publishing of the tagged image to **Docker Hub**.
- **Deployment Automation**: An **Ansible** playbook to automate the deployment of the application container on a target server.

## 🛠️ How to Run Locally

1.  **Prerequisites**: Docker and Docker Compose must be installed.
2.  Clone the repository:
    ```bash
    git clone [https://github.com/Pavel-Molchan/home-labe.git](https://github.com/Pavel-Molchan/home-labe.git)
    cd home-labe
    ```
3.  Build and start the services:
    ```bash
    docker-compose up --build
    ```
4.  Open your browser and navigate to `http://localhost:5000`.

## ⚙️ CI/CD Pipeline Breakdown

The pipeline, defined in `.github/workflows/main.yml`, consists of two main jobs:

1.  **`test`**: Runs on every push and pull request to the `main` branch. It checks out the code, installs dependencies, and runs the linter and unit tests to ensure the code is stable.
2.  **`build_and_push`**: This job is triggered only after the `test` job succeeds on a push to the `main` branch. It logs into Docker Hub and pushes the newly built image, making it ready for deployment.