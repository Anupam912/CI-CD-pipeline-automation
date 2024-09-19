# CI/CD Automation Project

This project automates the CI/CD process using GitHub Actions. It demonstrates how to build, test, and deploy an application in a seamless CI/CD pipeline, using both Python and PowerShell scripts for various tasks.

## Project Overview

The CI/CD pipeline includes the following automated steps:

1. Setup the environment using Python.
2. Build the application using PowerShell.
3. Run unit tests using Python.
4. Deploy the application using Docker and PowerShell.
5. Monitor deployment status using Python.
6. Each script is run in sequence in the CI/CD pipeline, ensuring an efficient, repeatable deployment process. \n

## Prerequisites

To run this project locally, you will need:

- Python 3.x installed.
- PowerShell (for Windows users) or `pwsh` (PowerShell Core on Linux/Mac).
- Docker installed and configured.
- GitHub repository set up for GitHub Actions.

## Local Setup Instructions

Follow these steps to run the scripts manually on your local machine:

1. Set up the Python environment and install dependencies:

    ```bash
    python python/setup.py
    ```

2. Build the application using the PowerShell script:

    ```bash
    powershell.exe -File powershell/build.ps1
    ```

3. Run unit tests using the Python test runner:

    ```bash
    python python/test_runner.py
    ```

4. Deploy the application using Docker and PowerShell:

    ```bash
    powershell.exe -File powershell/deploy.ps1
    ```

5. Monitor the status of the deployment using the Python deployment status checker:

    ```bash
    python python/deploy_status.py
    ```

## CI/CD Pipeline with GitHub Actions

The project uses *GitHub Actions* to automate the CI/CD pipeline. The workflow includes steps for building the Docker image, running unit tests, and deploying the application to a remote server.

### How It Works

The GitHub Actions workflow consists of two jobs:

1. **Build Job**: Builds the Docker image, tags it with the current Git commit hash, and pushes it to Docker Hub (or GitHub Container Registry).
2. **Deploy Job**: Connects to the remote server via SSH, pulls the Docker image, and updates the Docker service using zero-downtime deployment.

### GitHub Actions Workflow

The workflow file is located at `.github/workflows/ci-cd.yml`. The pipeline is triggered on a push to the main or master branch.

### Secrets Management in GitHub Actions

Handling sensitive information such as Docker credentials and SSH keys is managed through GitHub Actions ``Secrets``. Follow these steps to set up your secrets:

Handling sensitive information such as Docker credentials and SSH keys is managed through GitHub Actions Secrets. Follow these steps to set up your secrets:

1. Navigate to your repository on GitHub.
2. Click on the Settings tab.
3. In the left sidebar, select Secrets under Security.
4. Click New repository secret.
5. Add the following secrets:
    - DOCKER_USERNAME: Your Docker Hub or GHCR username.
    - DOCKER_PASSWORD: Your Docker Hub or GHCR password/token.
    - REMOTE_SERVER_HOST: The IP address or hostname of the remote server.
    - REMOTE_SERVER_USER: The SSH username for the remote server.
    - REMOTE_SERVER_SSH_KEY: Your private SSH key for connecting to the remote server.
    - Ensure that the secret names match exactly with those used in the ci-cd.yml file.
