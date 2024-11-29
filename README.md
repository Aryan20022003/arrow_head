# arrow_head

Backend Quant Developer Coding Task for Arrowhead Capital
Task Description
You are provided with three files:
1. Day Data File containing aggregated daily data, with columns:
- date: Date of the trading day.
- stock_name: Name of the stock.
- volume: Total volume traded for that stock on that day.
2. Intraday Second-by-Second Data Files for 19th April 2024 and 22nd April 2024, each
containing second-by-second trading data, with columns:
- date: Date of the trading day.
- timestamp: Timestamp for each second of the trading day.
- stock_name: Name of the stock.
- last_traded_quantity: Quantity of the stock traded in that specific second.
Objective
For each stock on 19th April 2024 and 22nd April 2024, determine the timestamp when the
cumulative traded volume within a rolling 60-minute window first exceeds the stock’s 30-day
average volume. This 30-day average is calculated from the 30 trading days preceding the
trading day. If no crossover occurs during the day, the output for that stock should be None.
Requirements
1. 30-Day Average Calculation: Compute the 30-day average volume for each stock for the
trading days 19th April 2024 and 22nd April 2024
2. Cumulative Volume Calculation: For each stock in the intraday data for 19th April 2024 and
22nd April 2024, calculate cumulative volume within a 60-minute rolling window, starting from
the market open at 9:15 AM.
3. Timestamp Identification: Identify the timestamp when the cumulative 60-minute volume
first surpasses the calculated 30-day average volume for each stock for the given dates. If no
such crossover occurs, the output should return None for that stock.
Constraints
The solution should be optimized for time complexity, as the datasets may contain large
amounts of data. The rolling calculation should be applied on a per-second basis, beginning from
market open.