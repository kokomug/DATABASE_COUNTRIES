# Deployment and Administration Guide for Python Flask Application with MongoDB on Azure Cosmos DB

## Introduction

This documentation functions as an extensive manual for the deployment and administration of a Python and Flask application that can scale efficiently while interacting with MongoDB on Azure Cosmos DB. The application is encapsulated using Docker and is deployed on Azure Kubernetes Service (AKS).

## Preparations

Ensure that you possess an active Azure account, and it is imperative to have Azure CLI installed for the subsequent procedures. It is a prerequisite to have Docker installed on your system to effectively proceed with the tasks outlined in this documentation.

## Step 1: Cosmos DB with MongoDB API through Azure Portal

1. **Resource Initiation**: Accessed Azure portal, setup a new Cosmos DB resource, choosing MongoDB API for Azure's managed database service.
2. **Performance Optimization (RU)**: Selected a serverless RU level for optimal database throughput, considering workload and cost.
3. **Database and Collection Setup**: Established 'countries_db' as the database and created a 'countries' collection within Cosmos DB.
4. **Data Upload**: Used Python scripts to upload JSON data to Cosmos DB, involving the extraction of the Primary Connection String for authentication within the script.

## Step 2: Python Scripting, RESTful API, and Docker Integration

1. **CRUD Operations**: Utilized the Python script `app.py` to perform Create, Read, Update, and Delete (CRUD) operations on the MongoDB database via the PyMongo driver.
2. **Dockerfile Creation**: Formulated a Dockerfile for encapsulating the Python Flask application, providing instructions for building a Docker image containing the app and its environment.
3. **Image Building with Commands**:
   - `docker build -t appy:latest`: Initiates Docker image construction from the Dockerfile.
   - `docker run -p 5000:5000 appy:latest`: Executes the container on port 5000.

## Step 3: ACR Setup and Docker Image Deployment

1. **Registry Creation**: Created an Azure Container Registry via the Azure portal for secure Docker image storage.
2. **ACR Configuration**: Configured ACR with a focus on access permissions and repository settings.
3. **Azure CLI Login**: Executed 'az login' for authentication and Azure CLI connectivity.
4. **Docker Image Tagging**: Used 'docker tag' to name the local image with ACR repository path.
5. **Push to ACR**: Uploaded the tagged image to Azure Container Registry using 'docker push,' ready for deployment on Azure services like AKS.

## Step 4: Azure Kubernetes Service (AKS) Cluster Launch with Network Configurations

1. **Virtual Network Setup**: Created a secure Azure virtual network for the AKS cluster.
   - Command: `az network vnet create -g resource_group_name -n yourVnetName --address-prefixes 10.0.0.0/8 --subnet-name yourSubnetName --subnet-prefix 10.240.0.0/16`
2. **Service Principal Creation**: Established a service principal using Azure CLI for AKS resource management. Using suitable commands.
3. **AKS Cluster Configuration**: Created the AKS cluster, specifying resource group, cluster name, node count, and network configurations.
   - Command: `az aks create -g ResourceGroupName -n ClusterName --node-count 1 --generate-ssh-keys --network-plugin azure --service-cidr 10.0.0.0/16 --dns-service-ip 10.0.0.10 --docker-bridge-address 172.17.0.1/16 --vnet-subnet-id SUBNET_ID --service-principal $SP_ID --client-secret $SP_PASSWORD --network-policy azure`
4. **Kubernetes Application Configuration**: Applied configuration files (ConfigMap, Deployment, Service YAML files) in Kubernetes using the Bash editor.
5. **Security Measures**: Ensured secure management of Kubernetes secrets, especially for sensitive data related to Cosmos DB and Azure Container Registry.
6. **Application Access**: Accessed the deployed application using the external IP address linked to the Kubernetes service.
   - Retrieve IP: `kubectl get svc appname-service`

## Step 5: Network Policies and Service Discovery in AKS

1. **Applying Network Policy**: Used the Kubernetes Bash Editor to apply a YAML-based network policy, ensuring secure data communication within the cluster.
2. **Testing Setup**: Conducted tests within the cluster to validate network policies, ensuring correct enforcement of traffic rules.
3. **Execution of Test Commands**: Tested endpoint access by running a temporary pod with an Alpine Linux image.
   - Command: `kubectl run -i --tty --rm debug --image=alpine --namespace=default --generator=run-pod/v1 --command -- /bin/sh -c "wget -O - http://yourEndpoint"`
4. **Service Discovery Purpose**: Implemented service discovery to enable seamless interaction between services in the Kubernetes cluster, particularly between the application and MongoDB.
5. **Service Discovery Method**: Configured Kubernetes services for dynamic discovery and communication, ensuring essential functionality and scalability.

## Contributing

Contributions to this project are welcome. If you'd like to contribute, please follow the guidelines outlined in the repository.

## License

This project is licensed under the Apache License 2.0.
