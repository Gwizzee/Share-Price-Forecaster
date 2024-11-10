Share Price Forecaster

A web app that provides a forecast of a stock's future price performance based on its historical data. It uses a simple moving average (SMA) for predictive analysis.

Disclaimer: This app is for educational purposes only and should not be used for actual trading. Stock market predictions are inherently complex and involve significant risk.

Features:

*   User input for stock symbol.
*   Fetches historical stock data using `yfinance`.
*   Calculates 20-day SMA.
*   Forecasts the next day's price as the last SMA value.
*   Web interface using Flask.

Requirements:

*   Python 3.7 or higher
*   Flask
*   yfinance
*   pandas

Installation:

1.  Clone the repository: `git clone <repository_url>`
2.  Install the necessary packages: `pip install -r requirements.txt`

Usage:

1.  Run the app: `python app.py`
2.  Open a web browser and go to `http://127.0.0.1:5000/`
3.  Enter a stock symbol (e.g., AAPL, MSFT) and click "Forecast".
4.  The predicted price will be displayed.

Limitations:

*   Uses a simplistic prediction model (SMA).
*   Relies solely on historical price data.
*   Does not account for external factors (news, economic events, etc.).

Future Releases:

*   Implementation of more prediction models.
*   Incorporating additional data sources.
*   Enhanced user interface and analysis filters.

 Contributing:

Contributions are welcome! Feel free to add features or submit pull requests.

License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE)   
 file for details.
