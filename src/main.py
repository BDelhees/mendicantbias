from loading_and_preparing_data import preparing_data
from process_data import process_data
from rnn_layer_fitting import fit_network
from prediction import predict


if __name__ == "__main__":
    df_train, df_test = preparing_data()

    X_train, y_train, scaler = process_data(df_train)
    fitted_regressor = fit_network(X_train, y_train)
    predicted_btc_price = predict(df_test, scaler, fitted_regressor)
    print(f"Predictions: {predicted_btc_price}")
