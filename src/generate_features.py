dataset.isnull().sum()
dataset = dataset.dropna()
dataset.shape
y = dataset['Class']
x = dataset [['Price','Package', 'Category','Rating']]
Y = y.values.reshape(1, -1)
X = x.values