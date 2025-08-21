import streamlit as st
from utils.data_fetch import fetch_screener_data
from utils.news import get_stock_news

st.title("Stock Screener (S&P 500)")

data = fetch_screener_data()

if data is not None:
    st.dataframe(data)

    selected_stock = st.selectbox("Select a stock for news", data['Ticker'])
    if selected_stock:
        st.subheader(f"Latest News for {selected_stock}")
        news_items = get_stock_news(selected_stock)
        if news_items:
            for n in news_items:
                st.write(f"**{n['headline']}** - {n['datetime']}")
                st.write(n['summary'])
                st.markdown("---")
else:
    st.warning("Unable to fetch screener data. Check API key.")
