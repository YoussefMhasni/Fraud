from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("KafkaStreamProcessor").getOrCreate()
spark.sql("""
  CREATE TEMPORARY TABLE kafka_table
  USING org.apache.spark.sql.kafka.KafkaSource
  OPTIONS (
    "kafka.bootstrap.servers" "localhost:9092",
    "subscribe" "testing"
  )
""")
# Read stream from Kafka
df = spark.readStream.table("kafka_table")
# Do some processing on the data


# Write the processed data to a console sink
query = df \
  .writeStream \
  .format("console") \
  .start()

query.awaitTermination()