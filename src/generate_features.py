dataset.isnull().sum()
dataset = dataset.dropna()
dataset.shape
y = dataset['Class']
x = dataset [['Price','Package', 'Category','Rating']]
Y = y.values.reshape(1, -1)
X = x.values
X_train, X_test, y_train, y_test = train_test_split(X, Y[0], test_size=0.2, random_state=1)