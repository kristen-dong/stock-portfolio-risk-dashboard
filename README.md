# Stock Portfolio Risk Dashboard

This project analyzes historical stock price data to evaluate portfolio performance and risk metrics such as annualized return, volatility, Sharpe ratio, and beta versus the market. It visualizes cumulative returns and provides a risk summary table to support investment decision-making.

## Key Features
- Pulls real stock data (AAPL, MSFT, GOOGL, AMZN, META) from Yahoo Finance
- Calculates daily returns, annual return, volatility, Sharpe ratio, and beta
- Visualizes cumulative portfolio returns over time
- Summarizes risk metrics in a clean table format

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- yFinance API

## Example Output
- Cumulative returns line chart
- Summary risk table with key investment metrics

## Notes
- Assumes equal weighting across selected stocks
- Risk-free rate assumed to be 0% for Sharpe Ratio calculation
