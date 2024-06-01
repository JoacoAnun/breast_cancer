# Breast Cancer Database Project

This project sets up a PostgreSQL database and pgAdmin for managing the database using Docker Compose.

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Data used on proyect](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset)

## Project Structure

.
├── docker-compose.yml

├── kafka_scripts/

        ├── kafka_consumer.py # Kafka consumer script
        └── kafka_producer.py # Kafka producer script 

├── sql_scritps

        └── table_creation.sql # SQL script to create tables

├── .env

├── postgres_vol/ # Volume for PostgreSQL data

└── pgadmin_vol/ # Volume for pgAdmin data


## Configuration

### .env File

Create a `.env` file in the root directory of the project and add the following content:

```plaintext
DATABASE_HOST=DATABASE_HOST
POSTGRES_USER=POSTGRES_USER
POSTGRES_PASSWORD=POSTGRES_PASSWORD
POSTGRES_DB=POSTGRES_DB
DB_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@localhost:5432/${POSTGRES_DB}"
PGADMIN_DEFAULT_EMAIL=PGADMIN_DEFAULT_EMAIL
PGADMIN_DEFAULT_PASSWORD=PGADMIN_DEFAULT_PASSWORD
TABLE_NAME=TABLE_NAME
CSV_PATH=CSV_PATH
Replace secure_postgres_password and secure_admin_password with your desired secure passwords.

The docker-compose.yml file and other scripts are configured to use the environment variables defined in the .env file.

