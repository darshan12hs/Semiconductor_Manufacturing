import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import joblib

df=pd.read_csv('PreProcessed.csv')
# print(df)

data=df.values

X=data[:,:-1]
y=data[:,-1]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

estimators=[
    ('lr', LogisticRegression(random_state=42)),
    ('rf', RandomForestClassifier(random_state=42)),
    ('dt', DecisionTreeClassifier(random_state=42)),
    ('svc', SVC(random_state=42)),
    ('knn', KNeighborsClassifier()),
    ('gnb', GaussianNB()),
    ('bnb', BernoulliNB())
]


voting_classifier=VotingClassifier(estimators=estimators)
voting_classifier.fit(X_train,y_train)

y_train_predict_1=voting_classifier.predict(X_train)
y_test_predict_1=voting_classifier.predict(X_test)

print("Train Accuracy before Hyperparameter tuning: \n",accuracy_score(y_train,y_train_predict_1))
print("Test Accuracy before Hyperparameter tuning: \n",accuracy_score(y_test,y_test_predict_1))

print("Confusion Matrix for Train Data: \n",confusion_matrix(y_train,y_train_predict_1))
print("Confusion Matrix for Test Data: \n",confusion_matrix(y_test,y_test_predict_1))

print("Classification Report for Train Data: \n",classification_report(y_train,y_train_predict_1))
print("Classification Report for Test Data: \n",classification_report(y_test,y_test_predict_1))

# Saving the model
joblib.dump(voting_classifier,"VC_model_file.pkl")


# vc=VotingClassifier(estimators=estimators)

# # Define the parameter grid for tuning
# param_grid = {
#     'lr__C': [0.1, 1, 10],
#     'rf__n_estimators': [50, 100],
#     'dt__max_depth': [None, 5, 10],
#     'svc__C': [0.1, 1, 10],
#     'knn__n_neighbors': [3, 5, 7],                # KNN hyperparameters
#     'gnb__var_smoothing': [1e-9, 1e-8, 1e-7],     # GaussianNB hyperparameters
#     'bnb__alpha': [0.1, 0.5, 1.0],             # BernoulliNB hyperparameters
#     'voting': ['hard', 'soft'],
# }

# grid_search=GridSearchCV(estimator=vc,param_grid=param_grid,cv=5)
# grid_search.fit(X_train,y_train)

# best_params=grid_search.best_params_
# print(best_params)

# best_vc=VotingClassifier(estimators=estimators,**best_params)
# best_vc.fit(X_train,y_train)

# y_train_predict_2=best_vc.predict(X_train)
# y_test_predict_2=best_vc.predict(X_test)

# print("Train Accuracy after hyperparameter tuning: \n",accuracy_score(y_train,y_train_predict_2))
# print("Test Accuracy after hyperparameter tuning: \n", accuracy_score(y_test,y_test_predict_2))

# print("Confusion Matrix for Train Data: \n",confusion_matrix(y_train,y_train_predict_1))
# print("Confusion Matrix for Test Data: \n",confusion_matrix(y_test,y_test_predict_1))

# print("Classification Report for Train Data: \n",classification_report(y_train,y_train_predict_2))
# print("Classification Report for Test Data: \n",classification_report(y_test,y_test_predict_2))

# # Saving the model
# joblib.dump(best_vc,"VC_model_file.pkl")
