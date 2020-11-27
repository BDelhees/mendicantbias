import numpy as np


def predict(df_test, sc, regressor):
    test_set = df_test.values
    inputs = np.reshape(test_set, (len(test_set), 1))
    inputs = sc.transform(inputs)
    inputs = np.reshape(inputs, (len(inputs), 1, 1))
    predicted_BTC_price = regressor.predict(inputs)
    predicted_BTC_price = sc.inverse_transform(predicted_BTC_price)

    return predicted_BTC_price


wandb.init(project="wandb-dstk", group=experiment1)


wandb.log({"predicted BTC Prices": predicted_BTC_prices})

print(predicted_BTC_prices)
print(test_set)
