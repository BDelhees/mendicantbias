import numpy as np
from sklearn.preprocessing import MinMaxScaler


def process_data(df_train):
    training_set = df_train.values
    training_set = np.reshape(training_set, (len(training_set), 1))
    sc = MinMaxScaler()
    training_set = sc.fit_transform(training_set)
    X_train = training_set[0 : len(training_set) - 1]
    y_train = training_set[1 : len(training_set)]
    X_train = np.reshape(X_train, (len(X_train), 1, 1))

    return X_train, y_train, sc
