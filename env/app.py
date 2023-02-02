from flask import Flask, render_template, jsonify, request, redirect, url_for
import subprocess
import json
import pandas as pd
from kafka import KafkaConsumer
import pickle
from flask import jsonify
from pandas import json_normalize
app = Flask(__name__)
consumer = KafkaConsumer('testing', bootstrap_servers=['localhost:9092'])    
import pandas as pd
@app.route('/df')
def data():
        print('hi1')
        with open('rf.pkl', 'rb') as file:
            model = pickle.load(file)
            for message in consumer:
                    print('hi2')
                    json_data = message.value.decode('utf-8')
                    dt = json.loads(json_data)
                    df= json_normalize(dt)
                    l=list(df.columns) 
                    for x in ['TransactionTime','cardType','TransactionID','DeviceType','card']:
                        l.remove(x)
                    prediction = model.predict(df[l])
                    fraud_data=dt
                    if prediction == 1 :
                        fraud_data["fraud_status"]= 1
                    else:
                        fraud_data["fraud_status"]= 0
                    json_string = json.dumps(fraud_data)
                    print(deserialize_message(json_string))
                    return deserialize_message(json_string)
def deserialize_message(json_data):
    data = json.loads(json_data)
    return {'Transaction ID':str(data["TransactionID"]),'Amount':str(data["TransactionAmt"]),"Date": str(pd.to_datetime(data["TransactionTime"])),'Device Type':data["DeviceType"],"fraud_status": str(data["fraud_status"])}

                        
@app.route('/')
def index():
        return render_template('idx.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)  