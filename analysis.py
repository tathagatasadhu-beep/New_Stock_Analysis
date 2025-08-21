import streamlit as st
from utils.data_fetch import fetch_analysis_data
from utils.charts import plot_fibonacci_chart

st.title("Stock Analysis")

ticker = st.text_input("Enter a Stock Ticker (e.g., AAPL)", "AAPL")

if ticker:
    analysis = fetch_analysis_data(ticker)
    if analysis:
        st.write(analysis)

    st.subheader("Fibonacci Retracement")
    fib_chart = plot_fibonacci_chart(ticker)
    if fib_chart:
        st.pyplot(fib_chart)
