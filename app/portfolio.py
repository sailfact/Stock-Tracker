import yfinance as yf

def get_price(ticker):
    try
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d')
        if not data.empty:
            return data['Close'].iloc[-1]
        else:
            return None
    except Exception as e:
        print(f"Error fetching price for {ticker}: {e}")
        return None