Full Stack Cloud Developer Project 4 - Kubernetes with EKS
Project Overview
This project involves deploying a Flask application on Kubernetes with AWS Elastic Kubernetes Service (EKS). The application is containerized using Docker and uses a Gunicorn server to serve the Flask application. It includes CI/CD integration using AWS CodePipeline and CodeBuild.

Requirements
Docker: For containerizing the Flask application.
Kubernetes: For orchestrating containers and deploying the application on AWS EKS.
AWS: For creating the infrastructure (EKS, Elastic Load Balancer, and Parameter Store).
Gunicorn: For serving the Flask application.
Setup Instructions
1. Docker Setup
The project uses python:stretch as the base image and gunicorn to serve the Flask app.
The Dockerfile sets up the environment and runs the application using Gunicorn.
2. Kubernetes Deployment
The application is deployed on AWS EKS using Kubernetes.
The Kubernetes configuration includes:
deployment.yml for deploying the application.
service.yml for exposing the app via LoadBalancer.
secret.yml for securely storing JWT_SECRET.
3. CI/CD Pipeline
AWS CodePipeline and CodeBuild are used to automate the build, test, and deployment of the application.
The application is tested using unit tests before deployment.
4. External URL (ELB)
The application is accessible via an Elastic Load Balancer (ELB), which was created automatically as part of the Kubernetes service setup.

ELB endpoint URL
http://a6d46f1485eef4d47a5cab98198588b2-2049829586.us-east-1.elb.amazonaws.com:80/

You can use the above ELB URL to access the running application.

Setup and Usage
1. Build the Docker image
To build the Docker image, use the following command:

bash
Copy code
docker build -t flask-app --build-arg JWT_SECRET=your_secret_key .
2. Run the Docker container locally
To run the container locally, use:

bash
Copy code
docker run -p 8080:8080 flask-app
You can access the application at http://localhost:8080.

3. Kubernetes Deployment on EKS
Create an EKS Cluster:

Set up an EKS cluster using AWS Console or AWS CLI.
Ensure that the Kubernetes kubectl configuration points to the correct context for your EKS cluster.
Apply Kubernetes configurations:

Apply the Kubernetes configuration files:
bash
Copy code
kubectl apply -f kubernetes/secret.yml
kubectl apply -f kubernetes/deployment.yml
kubectl apply -f kubernetes/service.yml
Get the ELB URL:

After deployment, run the following command to get the external URL (ELB URL):
bash
Copy code
kubectl get service flask-app-service
The URL will be shown under the EXTERNAL-IP or LoadBalancer Ingress column.

4. Accessing the Application
Once the application is deployed, you can access it through the ELB URL.

5. Testing
The application includes unit tests that are run during the CodeBuild phase in the CI/CD pipeline.

To run tests locally, use:

bash
Copy code
python -m unittest discover -s tests
Troubleshooting
Error when accessing the ELB URL: Make sure the Kubernetes service is exposed correctly and that the correct port is open on the LoadBalancer.
Missing dependencies in Docker: If there are missing dependencies, ensure that requirements.txt includes all necessary libraries.
Final Notes
The application is running successfully on AWS EKS and is exposed via an ELB.
All setup steps for deploying with Docker, Kubernetes, and EKS are documented.
Make sure to submit the ELB URL for your working application in the reviewer notes on Udacity.

