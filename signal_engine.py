def generate_signal(price, ma):
    if price > ma:
        print("EVENT: Bullish breakout detected")
        return "BUY"
    elif price < ma:
        print("EVENT: Bearish breakdown detected")
        return "SELL"
    else:
        return "HOLD"