import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import joblib

df=pd.read_csv("PreProcessed.csv")
# print(df)

data=df.values

X=data[:,:-1]
y=data[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=RandomForestClassifier(random_state=42)

model.fit(X_train,y_train)

y_train_predict_1=model.predict(X_train)
y_test_predict_1=model.predict(X_test)

print("Train Accuracy before Hyperparameter tuning: \n",accuracy_score(y_train,y_train_predict_1))
print("Test Accuracy before Hyperparameter tuning: \n",accuracy_score(y_test,y_test_predict_1))

print("Confusion Matrix for Train Data: \n",confusion_matrix(y_train,y_train_predict_1))
print("Confusion Matrix for Test Data: \n",confusion_matrix(y_test,y_test_predict_1))

print("Classification Report for Train Data: \n",classification_report(y_train,y_train_predict_1))
print("Classification Report for Test Data: \n",classification_report(y_test,y_test_predict_1))

rf_classifier=RandomForestClassifier(random_state=42)

# Define Hyperparameter grid for tuning 
param_grid={
    'n_estimators': [50,100,200],
    'max_depth': [None,5,10,20],
    'min_samples_split': [2,5,10],
    'min_samples_leaf': [1,2,4],
    'max_features': ['auto','sqrt','log2']
}

grid_search=GridSearchCV(estimator=rf_classifier,param_grid=param_grid,cv=5)
grid_search.fit(X_train,y_train)

best_params = grid_search.best_params_

print("Best Parameters: ",best_params)

best_rf_classifier=RandomForestClassifier(random_state=42, **best_params)
best_rf_classifier.fit(X_train,y_train)

y_train_predict_2=best_rf_classifier.predict(X_train)
y_test_predict_2=best_rf_classifier.predict(X_test)

print("Train Accuracy after hyperparameter tuning: \n",accuracy_score(y_train,y_train_predict_2))
print("Test Accuracy after hyperparameter tuning: \n", accuracy_score(y_test,y_test_predict_2))

print("Confusion Matrix for Train Data: \n",confusion_matrix(y_train,y_train_predict_1))
print("Confusion Matrix for Test Data: \n",confusion_matrix(y_test,y_test_predict_1))

print("Classification Report for Train Data: \n",classification_report(y_train,y_train_predict_2))
print("Classification Report for Test Data: \n",classification_report(y_test,y_test_predict_2))

# Saving the model
joblib.dump(best_rf_classifier,"RF_model_file.pkl")


