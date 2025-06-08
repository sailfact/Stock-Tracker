import streamlit as st

def display_portfolio(portfolio):
    holdings = portfolio.get_holdings()
    if holdings:
        st.subheader("Portfolio")
        total_value = 0
        total_cost = 0
        for ticker, data in holdings.items():
            price = portfolio.get_price(ticker)
            if price is None:
                st.warning(f"Could not fetch price for {ticker}")
                continue
            value = data["units"] * price
            cost = data["units"] * data["buy_price"]
            gain = value - cost
            total_value += value
            total_cost += cost
            st.write(f"**{ticker}**: {data['units']} units @ ${price:.2f} | Value: ${value:.2f} | Gain: ${gain:.2f}")

        st.write("---")
        st.metric("Total Value", f"${total_value:,.2f}")
        st.metric("Total Gain", f"${(total_value - total_cost):,.2f}")
    else:
        st.info("No holdings yet.")