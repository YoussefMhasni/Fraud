import pickle
import pandas as pd
df=pd.read_csv('validationdf.csv',header=0)
X_test=df.drop(['isFraud','Unnamed: 0'],axis=1)
y_test=df['isFraud']
with open('rf.pkl', 'rb') as file:
    model = pickle.load(file)
prediction = model.predict(X_test)
accuracy = model.score(X_test, y_test)
print('Accuracy:', accuracy)