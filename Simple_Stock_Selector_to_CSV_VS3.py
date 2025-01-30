import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Stock Data Downloader", page_icon="📉", layout="wide")

st.title("📈 Stock Data Downloader (Adj Close Only)")

# ✅ User Input for Stock Tickers
tickers = st.text_input("Enter stock tickers (comma separated):", "AAPL, MSFT, TSLA, GOOGL")
tickers = [ticker.strip().upper() for ticker in tickers.split(",")]

# ✅ Select Time Period
period = st.selectbox("Select Time Period:", ["1Y", "5Y", "MAX"])

# ✅ Fetch and Download Data
if st.button("Download Stock Data"):
    try:
        adj_close_data = yf.download(tickers, period=period.lower())["Adj Close"]  # ✅ Use yf.download()
        adj_close_data.dropna(axis=1, how="all", inplace=True)  # Remove tickers with no data

        if adj_close_data.empty:
            st.error("No valid stock data retrieved! Check tickers or time period.")
        else:
            csv = adj_close_data.to_csv(index=True)  # Convert to CSV
            st.success("Stock data retrieved successfully!")
            st.download_button(label="📥 Download CSV", data=csv, file_name="adj_close_data.csv", mime="text/csv")

    except Exception as e:
        st.error(f"Error fetching stock data: {e}")
