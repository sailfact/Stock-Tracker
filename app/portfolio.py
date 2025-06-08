import json
import os
import yfinance as yf

class Portfolio:
    def __init__(self, file_path):
        self.file_path = file_path
        self.holdings = self.load()

    def load(self):
        portfolio = {}
        # Check if the file exists and load the portfolio
        if os.path.exists(self.file_path):
            # Load the portfolio from the JSON file
            try:
                with open(self.file_path, 'r') as file:
                    portfolio = json.load(file)
            except json.JSONDecodeError:
                print("Error decoding JSON from the portfolio file.")
            except Exception as e:
                print(f"Unexpected error: {e}")

        return portfolio

    def save(self):
        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

        # Save the portfolio to the JSON file
        try:
            with open(self.file_path, 'w') as file:
                json.dump(self.holdings, file, indent=4)
        except Exception as e:
            print(f"Error saving portfolio: {e}")

    def get_price(ticker):
        try:
            stock = yf.Ticker(ticker)
            price = stock.info['last_price']
            return price
        except KeyError:
            print(f"Error retrieving price for {ticker}. Key not found.")
            return None
        
    def get_holdings(self):
        return self.holdings
        
    def buy(self, ticker, quantity, price, date):
        if ticker not in self.holdings:
            self.holdings[ticker] = {'quantity': 0, 'price': 0.0, 'date': date}
        
        current_quantity = self.holdings[ticker]['quantity']
        current_average_price = self.holdings[ticker]['average_price']
        
        # Calculate new average price
        new_average_price = (current_average_price * current_quantity + price * quantity) / (current_quantity + quantity)
        
        # Update holdings
        self.holdings[ticker]['quantity'] += quantity
        self.holdings[ticker]['rice'] = new_average_price
        self.holdings[ticker]['date'] = date
        
        # Save the updated portfolio
        self.save()
    
    def sell(self, ticker, quantity, price, date):
        if ticker in self.holdings:
            current_quantity = self.holdings[ticker]['quantity']
            if current_quantity >= quantity:
                # Update holdings
                self.holdings[ticker]['quantity'] -= quantity
                self.holdings[ticker]['date'] = date

                # Save the updated portfolio
                self.save()
            else:
                print(f"Not enough shares to sell for {ticker}.")
        else:
            print(f"No holdings found for {ticker}.")