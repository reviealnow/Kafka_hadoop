competition-kafka-hadoop-pipeline/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── k8s/
│   ├── kafka-deployment.yaml
│   ├── kafka-service.yaml
│   ├── zookeeper-deployment.yaml
│   ├── zookeeper-service.yaml
│   ├── producer-job.yaml
│   ├── mirror-deployment.yaml
│   └── mirror-configmap.yaml
├── docker/
│   └── producer.py
├── emr/
│   ├── bootstrap.sh
│   └── create-cluster.sh
├── spark/
│   └── kafka_to_hadoop.py
├── terraform/
│   ├── main.tf
│   └── variables.tf
├── README.md

# ► .github/workflows/deploy.yml
# GitHub Actions CI/CD pipeline

# ► k8s/zookeeper-deployment.yaml
# Kubernetes manifest for deploying Zookeeper

# ► k8s/zookeeper-service.yaml
# Zookeeper service definition

# ► k8s/kafka-deployment.yaml
# Kubernetes manifest for deploying Apache Kafka

# ► k8s/kafka-service.yaml
# Kafka service definition

# ► k8s/producer-job.yaml
# Kubernetes Job for running Kafka Producer

# ► k8s/mirror-deployment.yaml
# MirrorMaker 2 deployment on Kubernetes

# ► k8s/mirror-configmap.yaml
# MirrorMaker 2 configuration as ConfigMap

# ► docker/producer.py
# Sends JSON messages to local Kafka topic

# ► emr/bootstrap.sh
# Bootstrap for installing python libs on EMR

# ► emr/create-cluster.sh
# Shell script to create EMR cluster using AWS CLI

# ► spark/kafka_to_hadoop.py
# Spark Structured Streaming to consume from MSK and write to S3/HDFS

# ► terraform/main.tf
# Terraform script to create AWS MSK Cluster

# ► README.md
# Overview, Setup Steps, Diagrams, Usage
