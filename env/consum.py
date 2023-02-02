from kafka import KafkaConsumer
import json
from pandas import json_normalize
consumer = KafkaConsumer('testing', bootstrap_servers=['localhost:9092'])
import pickle
with open('env/rf.pkl', 'rb') as file:
    model = pickle.load(file)
    for message in consumer:
        json_data = message.value.decode('utf-8')
        data = json.loads(json_data)
        df = json_normalize(data)
        l=list(df.columns)
        for x in ['TransactionTime','cardType','TransactionID','DeviceType','card']:
            l.remove(x)
        prediction = model.predict(df[l])
        if prediction == 1 :
            print('Transaction is considered as a fraud !!!')
        else :
            print('transaction is completed')
consumer.close()