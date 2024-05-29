FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    pip install pyspark pandas faker

COPY generate_csv.py /app/generate_csv.py
COPY anonymize_data.py /app/anonymize_data.py
COPY ../data /app/data

WORKDIR /app

CMD ["bash"]