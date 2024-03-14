import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report,confusion_matrix
import joblib

df=pd.read_csv('PreProcessed.csv')
# print(df)

data=df.values
# print(data)

X=data[:,:-1]
y=data[:,-1]

# print(X)
# print(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

# Logistic Regression
model=LogisticRegression(random_state=42)

model.fit(X_train,y_train)

y_train_predict_1=model.predict(X_train)
y_test_predict_1=model.predict(X_test)

print("Train Accuracy before Hyperparameter tuning: \n",accuracy_score(y_train,y_train_predict_1))
print("Test Accuracy before Hyperparameter tuning: \n",accuracy_score(y_test,y_test_predict_1))

print("Confusion Matrix for Train Data: \n",confusion_matrix(y_train,y_train_predict_1))
print("Confusion Matrix for Test Data: \n",confusion_matrix(y_test,y_test_predict_1))

print("Classification Report for Train Data: \n",classification_report(y_train,y_train_predict_1))
print("Classification Report for Test Data: \n",classification_report(y_test,y_test_predict_1))

# Hyperparameter-Tuning
lr_model=LogisticRegression(random_state=42)

# Define HyperparametrerGrid For tuning
param_grid={
    'C':[0.01,0.1,1,10,100], #Regularization Parameter
    'penalty':['l1','l2'] #Regularization Type
}

# Initialize GridSearchCV
grid_search=GridSearchCV(lr_model, param_grid=param_grid,cv=5,scoring='accuracy')
grid_search.fit(X_train,y_train)


best_params = grid_search.best_params_

print("Best Parameters: ",best_params)

best_lr=LogisticRegression(random_state=42, **best_params)
best_lr.fit(X_train,y_train)

y_train_predict_2=best_lr.predict(X_train)
y_test_predict_2=best_lr.predict(X_test)

print("Train Accuracy after hyperparameter tuning: \n",accuracy_score(y_train,y_train_predict_2))
print("Test Accuracy after hyperparameter tuning: \n", accuracy_score(y_test,y_test_predict_2))

print("Confusion Matrix for Train Data: \n",confusion_matrix(y_train,y_train_predict_1))
print("Confusion Matrix for Test Data: \n",confusion_matrix(y_test,y_test_predict_1))

print("Classification Report for Train Data: \n",classification_report(y_train,y_train_predict_2))
print("Classification Report for Test Data: \n",classification_report(y_test,y_test_predict_2))

# Saving the model
joblib.dump(best_lr,"LR_model_file.pkl")



