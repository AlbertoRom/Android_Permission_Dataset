X_train, X_test, y_train, y_test = train_test_split(X, Y[0], test_size=0.2, random_state=1)

#Gradient Boosting Classifier
gbc = GradientBoostingClassifier()
gbc.fit(X_train, y_train)

#RidgeClassifier
rc = RidgeClassifier()
rc.fit(X_train, y_train)

#Gaussian Naive Bayes
gnb = GaussianNB()
gnb.fit(X_train, y_train)

#Random Forest Classifier
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)