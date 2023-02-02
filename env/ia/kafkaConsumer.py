# Import libraries
from kafka import KafkaConsumer
import json

topic_name = 'testing'

# Creata Kafka consumer, same default configuration frome the producer
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],

    # Deserialize the string from the producer since it comes in hex
    value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Message loader from Json
for message in consumer:
    tweets = json.loads(json.dumps(message.value))
    print(tweets)