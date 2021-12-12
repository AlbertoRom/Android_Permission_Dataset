#Gradient Boosting Classifier
predict_gbc = gbc.predict(X_test)
cr_gbc = classification_report(y_test, predict_gbc)
con_mat_gbc = confusion_matrix(y_test, predict_gbc)
mat_gbc = ConfusionMatrixDisplay(confusion_matrix=con_mat_gbc)

#RidgeClassifier
predict_rc = rc.predict(X_test)
cr_rc = classification_report(y_test, predict_rc)
con_mat_rc = confusion_matrix(y_test, predict_rc)
mat_rc = ConfusionMatrixDisplay(confusion_matrix=con_mat_rc)

#Gaussian Naive Bayes
predict_gnb = gnb.predict(X_test)
cr_gnb = classification_report(y_test, predict_gnb)
con_mat_gnb = confusion_matrix(y_test, predict_gnb)
mat_gnb = ConfusionMatrixDisplay(confusion_matrix=con_mat_gnb)

#Random Forest Classifier
predict_rfc = rfc.predict(X_test)
cr_rfc = classification_report(y_test, predict_rfc)
con_mat_rfc = confusion_matrix(y_test, predict_rfc)
mat_rfc = ConfusionMatrixDisplay(confusion_matrix=con_mat_rfc)