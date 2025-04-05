# Kafka_hadoop
The trial of AWS tryout
competition-kafka-hadoop-pipeline/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── k8s/
│   ├── kafka-deployment.yaml
│   ├── zookeeper-deployment.yaml
│   └── producer-job.yaml
├── docker/
│   └── producer.py
├── emr/
│   ├── bootstrap.sh
│   └── create-cluster.sh
├── mirrormaker/
│   ├── mirrormaker2.properties
│   └── mirror-launch.sh
├── spark/
│   └── kafka_to_hadoop.py
├── terraform/
│   ├── main.tf
│   └── variables.tf
├── README.md

# ► .github/workflows/deploy.yml
# GitHub Actions CI/CD pipeline

# ► k8s/kafka-deployment.yaml
# Kubernetes manifest for deploying Apache Kafka

# ► k8s/zookeeper-deployment.yaml
# Kubernetes manifest for deploying Zookeeper

# ► k8s/producer-job.yaml
# Kubernetes Job for running Kafka Producer

# ► docker/producer.py
# Sends JSON messages to local Kafka topic

# ► mirrormaker/mirrormaker2.properties
# Kafka MirrorMaker2 config for syncing local to AWS MSK

# ► mirrormaker/mirror-launch.sh
# Bash script to launch MirrorMaker

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
