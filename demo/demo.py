import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import RidgeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.metrics import plot_confusion_matrix

pd.set_option('display.float_format', lambda x: '%.3f' % x)

def load_dataset(path):
    dataset = pd.read_csv(path, header=0, delimiter=',')
    return dataset

dataset = load_dataset('../data/Android_Permission.csv')

label_encoder = preprocessing.LabelEncoder()
dataset_copia = dataset.copy()
dataset['Category'] = label_encoder.fit_transform(dataset['Category'])
dataset['Package'] = label_encoder.fit_transform(dataset['Package'])

dataset.isnull().sum()
dataset = dataset.dropna()
dataset.shape
y = dataset['Class']
x = dataset [['Price','Package', 'Category','Rating']]
Y = y.values.reshape(1, -1)
X = x.values

X_train, X_test, y_train, y_test = train_test_split(X, Y[0], test_size=0.2, random_state=1)

#Gradient Boosting Classifier
print("Gradient Boosting Classifier")
gbc = GradientBoostingClassifier()
gbc.fit(X_train, y_train)
predict_gbc = gbc.predict(X_test)
cr_gbc = classification_report(y_test, predict_gbc)
con_mat_gbc = confusion_matrix(y_test, predict_gbc)
print(cr_gbc)
sns.heatmap(con_mat_gbc, annot=True, fmt='.4g', cmap='Greens')
plt.show()

#Ridge Classifier
print("Ridge Classifier")
rc = RidgeClassifier()
rc.fit(X_train, y_train)
predict_rc = rc.predict(X_test)
cr_rc = classification_report(y_test, predict_rc)
con_mat_rc = confusion_matrix(y_test, predict_rc)
print(cr_rc)
sns.heatmap(con_mat_rc, annot=True, fmt='.4g', cmap='Greens')
plt.show()


#Gaussian Naive Bayes
print("Gaussian Naive Bayes")
gnb = GaussianNB()
gnb.fit(X_train, y_train)
predict_gnb = gnb.predict(X_test)
cr_gnb = classification_report(y_test, predict_gnb)
con_mat_gnb = confusion_matrix(y_test, predict_gnb)
print(cr_gnb)
sns.heatmap(con_mat_gnb, annot=True, fmt='.4g', cmap='Greens')
plt.show()


#Random Forest Classifier
print("Random Forest Classifier")
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
predict_rfc = rfc.predict(X_test)
cr_rfc = classification_report(y_test, predict_rfc)
con_mat_rfc = confusion_matrix(y_test, predict_rfc)
print(cr_rfc)
sns.heatmap(con_mat_rfc, annot=True, fmt='.4g', cmap='Greens')
plt.show()

#Regressió Logistica
print("Regressió Logistica")
lr = LogisticRegression()
lr.fit(X_train,y_train)
predict_lr = lr.predict(X_test)
cr_lr = classification_report(y_test, predict_lr)
con_mat_lr = confusion_matrix(y_test, predict_lr)
print(cr_lr)
sns.heatmap(con_mat_lr, annot=True, fmt='.4g', cmap='Greens')
plt.show()
