from kafka import KafkaProducer
import pandas as pd
import time
import csv

# create a Kafka producer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                        value_serializer=lambda x: x.encode('utf-8'))

df=pd.read_csv('validation.csv',header=0)
copy=df.copy()
X=df.drop(['isFraud'],axis=1)
for index, row in X.iterrows():
    producer.send('testing', value=row.to_json())
    time.sleep(3)
producer.flush()
producer.close()

