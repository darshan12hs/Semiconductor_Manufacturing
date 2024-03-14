import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import joblib

df=pd.read_csv("PreProcessed.csv")
# print(df)

data=df.values

X=data[:,:-1]
y=data[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=BernoulliNB()
model.fit(X_train,y_train)

y_train_predict_1=model.predict(X_train)
y_test_predict_1=model.predict(X_test)

print("Train Accuracy before Hyperparameter tuning: \n",accuracy_score(y_train,y_train_predict_1))
print("Test Accuracy before Hyperparameter tuning: \n",accuracy_score(y_test,y_test_predict_1))

print("Confusion Matrix for Train Data: \n",confusion_matrix(y_train,y_train_predict_1))
print("Confusion Matrix for Test Data: \n",confusion_matrix(y_test,y_test_predict_1))

print("Classification Report for Train Data: \n",classification_report(y_train,y_train_predict_1))
print("Classification Report for Test Data: \n",classification_report(y_test,y_test_predict_1))

bnb_model=BernoulliNB()

# Define Hyperparameter grid for tuning 
param_grid={
    'alpha': [0.1, 0.5, 1.0, 2.0, 5.0]  # Smoothing parameter values to test
}

grid_search=GridSearchCV(estimator=bnb_model,param_grid=param_grid,cv=5)
grid_search.fit(X_train,y_train)

best_params = grid_search.best_params_

print("Best Parameters: ",best_params)

best_bnb_model=BernoulliNB(**best_params)
best_bnb_model.fit(X_train,y_train)

y_train_predict_2=best_bnb_model.predict(X_train)
y_test_predict_2=best_bnb_model.predict(X_test)

print("Train Accuracy after hyperparameter tuning: \n",accuracy_score(y_train,y_train_predict_2))
print("Test Accuracy after hyperparameter tuning: \n", accuracy_score(y_test,y_test_predict_2))

print("Confusion Matrix for Train Data: \n",confusion_matrix(y_train,y_train_predict_1))
print("Confusion Matrix for Test Data: \n",confusion_matrix(y_test,y_test_predict_1))

print("Classification Report for Train Data: \n",classification_report(y_train,y_train_predict_2))
print("Classification Report for Test Data: \n",classification_report(y_test,y_test_predict_2))

# Saving the model
joblib.dump(best_bnb_model,"BNB_model_file.pkl")