# Kubernetes-Deployment-using-Jenkins-GitHub-and-Argo-CD
Automated Kubernetes Deployment using Jenkins, GitHub, and Argo CD

# Project: Automated Kubernetes Deployment using Jenkins, GitHub, and Argo CD

## Overview:
In this project, we demonstrate an automated deployment pipeline to deploy an application to a Kubernetes cluster utilizing Jenkins, GitHub, and Argo CD. This setup showcases how code changes in GitHub trigger a Jenkins job, which in turn builds a Docker image, pushes it to Docker Hub, updates the Kubernetes manifests, and triggers Argo CD to sync the changes to the Kubernetes cluster.

## Topics Covered:
- GitHub workflow for demo and contrast with traditional DevOps workflow.
- Dockerfile and Jenkinsfile walkthrough.
- Jenkins installation and job setup.
- Argo CD installation and setup.
- Automating GitHub to Jenkins using webhook.
- Zero touch end-to-end automation, achieving a state of nirvana.

## Repositories:
1. **Kubernetes Code Repository**: Contains `app.py` (simple Flask application) and Dockerfile to dockerize the application.
2. **Kubernetes Manifest Repository**: Contains `deployment.yaml` and Jenkinsfile for updating the Kubernetes deployment manifest.

## Jenkins Jobs:
1. **Build Image Job**: 
   - Clones the Kubernetes Code repository.
   - Builds a Docker container image with a new tag.
   - Pushes the Docker image to Docker Hub.
   - Triggers the Update Manifest job with the new image tag.
   
2. **Update Manifest Job**:
   - Clones the Kubernetes Manifest repository.
   - Updates `deployment.yaml` with the new image tag.
   - Commits and pushes the changes to GitHub.

## Argo CD Setup:
- Argo CD continuously monitors the Kubernetes Manifest repository.
- On detecting a change, it syncs the Kubernetes cluster to match the state defined in the repository.

## Workflow Steps:
1. Developer makes a code change in `app.py` and pushes it to the Kubernetes Code repository on GitHub.
2. This triggers the Build Image job in Jenkins.
3. Build Image job creates a new Docker image, pushes it to Docker Hub, and triggers the Update Manifest job with the new image tag.
4. Update Manifest job updates the `deployment.yaml` in the Kubernetes Manifest repository with the new image tag and pushes the changes to GitHub.
5. Argo CD detects the change in Kubernetes Manifest repository, and syncs the Kubernetes cluster to deploy the new image.

## Automation:
- A webhook is set up in GitHub to trigger the Build Image job in Jenkins upon a code push.
- Argo CD is configured to automatically sync the Kubernetes cluster with the state defined in the Kubernetes Manifest repository.

## Outcome:
By the end of this setup, we achieve a fully automated CI/CD pipeline where code changes are seamlessly deployed to the Kubernetes cluster without any manual intervention, illustrating the power of integrating Jenkins, GitHub, and Argo CD in a Kubernetes environment.

## Demonstration:
A detailed video demonstration of this project walks through each step, explaining the configuration, the rationale behind the setup, and showcasing the end-to-end automation in action. 

---


This README provides a structured overview of the project, encapsulating the major aspects, the setup, and the workflow in a concise manner.
