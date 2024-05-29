from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sha2

def anonymize_data(input_file, output_file):
    spark = SparkSession.builder.appName("Anonymizer").getOrCreate()
    
    df = spark.read.csv(input_file, header=True)
    
    df_anonymized = df.withColumn("first_name", sha2(col("first_name"), 256)) \
                      .withColumn("last_name", sha2(col("last_name"), 256)) \
                      .withColumn("address", sha2(col("address"), 256))
    
    df_anonymized.write.csv(output_file, header=True)

if __name__ == "__main__":
    anonymize_data('../data/input.csv', '../data/anonymized_output.csv')