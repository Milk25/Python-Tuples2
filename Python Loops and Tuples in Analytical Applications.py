def average_closing_price(stock_data, stock_symbol, start_date, end_date):
    total_price = 0
    count = 0
    
    for symbol, date, price in stock_data:
        if symbol == stock_symbol and start_date <= date <= end_date:
            total_price += price
            count += 1
    
    if count == 0:
        return None  # No data found for the specified stock and period
    else:
        return total_price / count

# Sample data
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

# Example usage
avg_price = average_closing_price(stock_data, "AAPL", "2021-01-01", "2021-01-02")
if avg_price is not None:
    print(f"Average closing price of AAPL from 2021-01-01 to 2021-01-02: ${avg_price:.2f}")
else:
    print("No data found for the specified stock and period.")