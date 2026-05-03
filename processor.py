import pandas as pd

def compute_features(prices):
    df = pd.DataFrame(prices, columns=["price"])

    df["returns"] = df["price"].pct_change()
    df["volatility"] = df["returns"].rolling(5).std()

    df["ma"] = df["price"].rolling(5).mean()

    return df.iloc[-1].to_dict()