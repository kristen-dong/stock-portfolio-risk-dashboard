# Stock Portfolio Risk Dashboard Project

# --- Imports ---
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

# --- Step 1: Pull Stock Price Data ---
stocks = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META']
start_date = '2022-01-01'
end_date = '2023-12-31'

data = yf.download(stocks, start=start_date, end=end_date)['Adj Close']

# --- Step 2: Calculate Daily Returns ---
daily_returns = data.pct_change().dropna()

# --- Step 3: Assume Equal Weights Portfolio ---
weights = np.array([1/len(stocks)] * len(stocks))
portfolio_returns = daily_returns.dot(weights)

# --- Step 4: Calculate Risk Metrics ---
# Annualized Volatility
volatility = np.std(portfolio_returns) * np.sqrt(252)

# Annualized Return
annual_return = np.mean(portfolio_returns) * 252

# Sharpe Ratio (Assuming risk-free rate ~ 0%)
sharpe_ratio = annual_return / volatility

# Beta (against S&P 500)
spy = yf.download('SPY', start=start_date, end=end_date)['Adj Close']
spy_returns = spy.pct_change().dropna()

covariance = np.cov(portfolio_returns, spy_returns)[0][1]
market_variance = np.var(spy_returns)
beta = covariance / market_variance

# --- Step 5: Visualization ---
cumulative_returns = (1 + portfolio_returns).cumprod()

plt.figure(figsize=(10,6))
plt.plot(cumulative_returns, label='Portfolio Cumulative Return')
plt.title('Portfolio Cumulative Returns')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.legend()
plt.grid(True)
plt.show()

# --- Step 6: Summary Table ---
summary = pd.DataFrame({
    'Annual Return': [annual_return],
    'Volatility': [volatility],
    'Sharpe Ratio': [sharpe_ratio],
    'Beta vs S&P500': [beta]
})

print("\nPortfolio Risk Metrics Summary:")
print(summary.round(4))
