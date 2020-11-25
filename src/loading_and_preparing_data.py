import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import wandb


# Import the dataset and encode the date


def preparing_data():
    df = pd.read_csv("bitcoin.csv")
    import pdb

    pdb.set_trace()  # XXX BREAKPOINT

    df["date"] = pd.to_datetime(df["Timestamp"], unit="s").dt.date
    # df["date"] = df["date"].astype("datetime64[ns]")
    group = df.groupby("date")
    Real_Price = group["Weighted_Price"].mean()
    # split data
    prediction_days = 3
    df_train = Real_Price[: len(Real_Price) - prediction_days]
    df_test = Real_Price[len(Real_Price) - prediction_days :]

    return df_train, df_test

# Weights and Biases

wandab.init(project="ds-tk")

# Log metrics with wandb
 
for _ in range(num_epochs):
  train_model()
  loss = calulate_loss()
  wandb.log({"Loss": loss})

# Save model to wandb

np.save("weights", weights)
wandb.save("weights.npy")


