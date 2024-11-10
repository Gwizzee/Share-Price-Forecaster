from flask import Flask, render_template, request
import yfinance as yf
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        stock_symbol = request.form["stock_symbol"]
        try:
            # Download historical data
            stock_data = yf.download(stock_symbol, period="5y")

            # Calculate simple moving average (20 days)
            stock_data["SMA"] = stock_data["Close"].rolling(window=20).mean()

            # Forecast: assume next day's price is the same as the SMA
            forecast = stock_data["SMA"].iloc[-1]

            return render_template("result.html", stock_symbol=stock_symbol, forecast=forecast)
        except:
            return "Error fetching stock data. Please check the symbol."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
