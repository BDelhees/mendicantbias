#process data
training_set=df_train.values
training_set=np.reshape(training_set, (len(training_set), 1))
sc=MinMaxScaler()
training_set=sc.fit_transform(training_set)
X_train= training_set[0:len(training_set)-1]
y_train= training_set[1:len(training_set)]
X_train= np.reshape(X_train, (len(X_train), 1, 1))

# Initialising the RNN
regressor = Sequential()

# Adding the input layer and the LSTM layer
regressor.add(LSTM(units = 4, activation = 'sigmoid', input_shape = (None, 1)))

# Adding the output layer
regressor.add(Dense(units = 1))

# Compiling the RNNregressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

