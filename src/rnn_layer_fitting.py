from tensorflow.keras import Sequential
from tensorflow.keras.layers import LSTM, Dense


def fit_network(X_train, y_train):
    # Initialising the RNN
    regressor = Sequential()

    # Adding the input layer and the LSTM layer
    regressor.add(LSTM(units=4, activation="sigmoid", input_shape=(None, 1)))

    # Adding the output layer
    regressor.add(Dense(units=1))

    # Compiling the RNNregressor.compile(optimizer = 'adam', loss = 'mean_squared_error')
    regressor.compile(optimizer="adam", loss="mean_squared_error")

    # Fitting the RNN to the Training set
    regressor.fit(X_train, y_train, batch_size=5, epochs=100)

    return regressor

regressor.compile(optimizer=config.optimizer,
              loss=config.loss
              )

history = model.fit(x=X_train,
                    y=y_train,
                    epochs=config.epoch,
                    batch_size=config.batch_size,
                    validation_data=(test_set),
                    callbacks=[WandbCallback()])


wandb.finish()
