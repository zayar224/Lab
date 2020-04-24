### Note: First You Need To Install xlrd To Read The Excel File ###
### This Program Can Check 3 Kinds Of Text ("Myanmar", "English", "Myanglish")

import numpy as np 
import pandas as pd 

df = pd.read_excel("test1.xlsx", sep='\t') #encoding='utf-8-sig'

df.isnull().sum() #check for missing values

### Split the data Traning and Test set
from sklearn.model_selection import train_test_split

X = df['sentence']
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42 )

### Pipeline
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

## Create Pipeline Object
text_clf = Pipeline([('tfidf' , TfidfVectorizer()),
	('clf', LinearSVC())])
## train (or) fit Pipeline
text_clf.fit(X_train, y_train)

### Predictions
predictions = text_clf.predict(X_test)

### Compare X to y label data
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

#print(confusion_matrix(y_test, predictions)) #Confusion Matrix

## Check Classification Report
#print(classification_report(y_test, predictions))

## Accurancy Score
print("Accurancy Score is ", accuracy_score(y_test, predictions).round(2))
print(text_clf.predict(["Myanmar is my native language."])) ## You can type whatever you want to check what type of text is it ##