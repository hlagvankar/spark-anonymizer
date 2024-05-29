# Spark Anonymizer

## Overview

This project generates a CSV file with synthetic data and then anonymizes specific columns using PySpark.

## Project Structure

- `src/`: Contains the Python scripts and Dockerfile.
- `data/`: Directory to store input and output CSV files.
- `tests/`: Directory for test scripts.
- `README.md`: This file.

## Setup

### Prerequisites

- Docker
- Docker Compose (optional)

### Build Docker Image

```bash
docker build -t spark-anonymizer src/

Run the Container

docker run --rm -v $(pwd)/data:/app/data spark-anonymizer python generate_csv.py
docker run --rm -v $(pwd)/data:/app/data spark-anonymizer python anonymize_data.py
