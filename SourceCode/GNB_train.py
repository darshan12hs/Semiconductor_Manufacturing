import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import joblib

df=pd.read_csv("PreProcessed.csv")
# print(df)

data=df.values

X=data[:,:-1]
y=data[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

gnb_model=GaussianNB()

gnb_model.fit(X_train,y_train)

y_train_predict=gnb_model.predict(X_train)
y_test_predict=gnb_model.predict(X_test)

print("Train Accuracy: \n",accuracy_score(y_train,y_train_predict))
print("Test Accuracy: \n",accuracy_score(y_test,y_test_predict))

print("Confusion Matrix for Train Data: \n",confusion_matrix(y_train,y_train_predict))
print("Confusion Matrix for Test Data: \n",confusion_matrix(y_test,y_test_predict))

print("Classification Report for Train Data: \n",classification_report(y_train,y_train_predict))
print("Classification Report for Test Data: \n",classification_report(y_test,y_test_predict))

# Saving the model
joblib.dump(gnb_model,"GNB_model_file.pkl")