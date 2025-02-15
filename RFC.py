import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report ,accuracy_score,confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

iris=load_iris()
X,y=iris.data,iris.target

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

rf_clf=RandomForestClassifier(n_estimators=100,random_state=42)
rf_clf.fit(X_train,y_train)

y_pred=rf_clf.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy:{accuracy:.2f}")
print("Classification report")
print(classification_report(y_test,y_pred,target_names=iris.target_names))
conf_matrix=confusion_matrix(y_test,y_pred)
print("Confusion matrix")
print(conf_matrix)
plt.figure(figsize=(8,6))
sns.heatmap(conf_matrix,annot=True,fmt='d',cmap="Blues",xticklabels=iris.target_names,yticklabels=iris.target_names)
plt.ylabel('actual')
plt.xlabel('predicted')
plt.title('confusion matrix')
plt.show()