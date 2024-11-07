import streamlit as st
import yfinance as yf
import datetime 

ticker_symbol=st.text_input("Enter ticker_symbol(AAPL-for Apple, GOOG-for Google ,MSFT-for Microsoft):")#Recent Added
ticker_data=yf.Ticker(ticker_symbol)

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Enter Start Date", datetime.date(2022, 1, 1))
with col2:
    end_date = st.date_input("Enter End Date", datetime.date(2024, 10, 1))


ticker_df=ticker_data.history(period="1d", start=start_date,end=end_date)
st.title("Stock Price Analyzer")
st.write("here is the row day wise stock movement:")
st.dataframe(ticker_df)


st.write("Price Movement Over Time")
st.line_chart(ticker_df['Close'])

st.write("Volume Movement Over Time")
st.line_chart(ticker_df['Volume'])
