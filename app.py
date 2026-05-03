from fastapi import FastAPI
from data_fetcher import get_price
from processor import compute_features
from signal_engine import generate_signal

app = FastAPI()

price_history = []

@app.get("/")
def home():
    return {"message": "Trading Backend Running"}

@app.get("/price")
def price():
    price = get_price()
    price_history.append(price)

    if len(price_history) > 50:
        price_history.pop(0)

    return {"price": price}

@app.get("/features")
def features():
    if len(price_history) < 5:
        return {"error": "Not enough data"}

    return compute_features(price_history)

@app.get("/signal")
def signal():
    if len(price_history) < 5:
        return {"error": "Not enough data"}

    features = compute_features(price_history)
    sig = generate_signal(features["price"], features["ma"])

    return {
        "signal": sig,
        "price": features["price"],
        "moving_avg": features["ma"]
    }