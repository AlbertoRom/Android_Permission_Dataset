#Gradient Boosting Classifier
gbc = GradientBoostingClassifier()
gbc.fit(X_train, y_train)

#Ridge Classifier
rc = RidgeClassifier()
rc.fit(X_train, y_train)

#Gaussian Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train, y_train)

#Random Forest Classifier
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)

#Regressió Logistica
lr = LogisticRegression()
lr.fit(X_train,y_train)