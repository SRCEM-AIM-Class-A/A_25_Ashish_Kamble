# Django Project with Docker and Jenkins

## Overview
This repository contains a Django project containerized using Docker with CI/CD automation using Jenkins. The setup allows for easy deployment and local development without manual configuration of dependencies.

## Prerequisites
Ensure you have the following installed:
- [Docker](https://www.docker.com/get-started)
- [Jenkins](https://www.jenkins.io/)

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/SRCEM-AIM-Class-A/A_25_Ashish_Kamble.git
```

### 2. Build the Docker Image
```sh
docker build -t my-django-app .
```

### 3. Run the Container
```sh
docker run -d -p 8000:8000 --name django-container my-django-app
```

### 4. Access the Application
Open a browser and go to:
```
http://localhost:8000
```

### 5. Check Running Containers
```sh
docker ps
```

## Setting Up Jenkins for CI/CD

### 1. Run Jenkins in a Docker Container
```sh
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins-container jenkins/jenkins:lts
```

### 2. Access Jenkins Dashboard
Open a browser and go to:
```
http://localhost:8080
```

### 3. Get Jenkins Initial Admin Password
```sh
docker exec jenkins-container cat /var/jenkins_home/secrets/initialAdminPassword
```
Use this password to log in to Jenkins.

### 4. Install Necessary Plugins
- Install recommended plugins during setup.
- Add Docker and GitHub plugins if needed.

### 5. Configure a Jenkins Pipeline
- Create a new pipeline job in Jenkins.
- Use a `Jenkinsfile` for automation.

## Pushing the Image to Docker Hub

### 1. Log in to Docker Hub
```sh
docker login
```

### 2. Tag the Image
```sh
docker tag my-django-app your-dockerhub-username/my-django-app:latest
```

### 3. Push the Image
```sh
docker push your-dockerhub-username/my-django-app:latest
```

## Stopping and Removing Containers
```sh
docker stop django-container
docker rm django-container
```

## Useful Docker Commands
- View logs: `docker logs django-container`
- Enter container shell: `docker exec -it django-container /bin/sh`
- Remove image: `docker rmi my-django-app`

---

Happy Coding! 🚀

