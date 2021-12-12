#Gradient Boosting Classifier
gbc = GradientBoostingClassifier()
gbc.fit(X_train, y_train)
dump(predict_gbc, '../models/gbc.joblib')

#Ridge Classifier
rc = RidgeClassifier()
rc.fit(X_train, y_train)
dump(predict_gbc, '../models/rc.joblib')

#Gaussian Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train, y_train)
dump(predict_gbc, '../models/gnb.joblib')

#Random Forest Classifier
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
dump(predict_gbc, '../models/rfc.joblib')

#Regressió Logistica
lr = LogisticRegression()
lr.fit(X_train,y_train)
dump(predict_gbc, '../models/lr.joblib')