## Automation Data Pipeline

This repository contains an automated data pipeline built using PySpark, Airflow, and MongoDB/PostgreSQL, designed to streamline the process of data extraction, transformation, validation, and loading into a data warehouse.

The pipeline was developed as part of a data engineering project, with a focus on scalability, reliability, and data quality assurance.

### Features

- Data Extraction (ETL)
Automatically extracts raw data from multiple sources (e.g., APIs, CSVs, databases).

- Data Cleaning & Transformation
Handles missing values, standardizes formats, and applies business logic with PySpark.

- Data Validation with Great Expectations
Ensures data quality by validating schema, null values, duplicates, and business rules.

- Workflow Orchestration
Automated scheduling and monitoring using Apache Airflow.

- Data Loading
Transforms and loads data into PostgreSQL / Data Warehouse for further analytics.

- Modular Design
Each step (extract → clean → transform → validate → load) is built as independent tasks for flexibility and maintainability.

### Tech Stack

- Apache Airflow – Workflow orchestration

- PySpark – Distributed data processing

- MongoDB – Source database

- PostgreSQL – Data warehouse

- Great Expectations – Data quality & validation

- Docker – Containerization for portability

### Use Cases

- Automating recurring ETL jobs

- Building reliable data pipelines for analytics

- Ensuring high data quality for dashboards & BI tools

- Enabling scalable data engineering workflows
