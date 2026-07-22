# Apache-Kafka-Stream

Apache Kafka Producer-Consumer (Python + Docker)

A minimal Apache Kafka setup running in KRaft mode (no ZooKeeper) via Docker Compose, with Python producer and consumer scripts for sending and reading messages.

Stack

Python — producer/consumer clients
Docker / Docker Compose — containerized Kafka broker
Apache Kafka (Confluent cp-kafka:8.2.2, KRaft mode)

Project Structure
.
├── producer.py         # Publishes messages to a Kafka topic
├── consumer.py         # Subscribes to and reads messages from a Kafka topic
├── docker-compose.yaml # Kafka broker service definition (KRaft mode, single node)
└── requirements.txt    # Python dependencies

Prerequisites

Docker and Docker Compose
Python 3.10+ (using 3.12 for this project)
pip

Notes

This setup uses a single-broker, single-controller KRaft cluster intended for local development only — it is not configured for production (no replication, no authentication, no TLS).

KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR is set to 1 since there's only one broker.
