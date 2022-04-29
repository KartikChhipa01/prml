import streamlit as st
import datetime
import pandas as pd
def app():
    st.title('APP2')
    st.subheader('Predict the Bitcoin Prices on a particular Date')
    st.write('Note that the maximum date upto which we can predict the bitcoin prices is 20 dates. Predicted the prices of further days is not possible be Bitcoin Prices depend on many other paramaters')
    date=st.date_input("Enter the Date for which you want to know the price of Bitcoin",value=datetime.date(2022,2,20),max_value=datetime.date(2022,3,11))
    data=pd.read_csv('https://raw.githubusercontent.com/KartikChhipa01/datasets/main/BTC-USD.csv')
    st.table(data)