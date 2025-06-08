# main.py

import streamlit as st
from portfolio import Portfolio
from display import display_portfolio

PORTFOLIO_FILE = "data/portfolio.json"

def app():
    st.title("📈 ETF Portfolio Tracker")
    portfolio = Portfolio(PORTFOLIO_FILE)

    # Add New Ticker
    with st.form("add_form"):
        st.subheader("Add Holding")
        ticker = st.text_input("Ticker (e.g. VAS.AX)").upper()
        units = st.number_input("Units", min_value=0.0, step=1.0)
        buy_price = st.number_input("Buy Price", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Add")
        if submitted and ticker and units:
            portfolio.add_holding(ticker, units, buy_price)
            st.success(f"Added {ticker}")

    display_portfolio(portfolio)

if __name__ == "__main__":
    app()