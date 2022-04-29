# app2.py
from datetime import datetime
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
def app():
    data=pd.read_csv('https://raw.githubusercontent.com/KartikChhipa01/datasets/main/BTC-USD.csv')
    st.title('Dataset used for the Project')
    st.write('Below is the Dataset used for the project. The dataset contains the information about the bitcoin')
    st.write('Open - The opening price of the crypto asset for the day')
    st.write('Close - The cash value of the last transacted price before the market close')
    st.write('High - The highest Price of the crypto asset of the day')
    st.write('Low - The lowest price of the crypto asset for the day')
    st.write('Volume - The total number of cryto asset being exchanged in a day')
    st.write('Adj Close The adjusted closing price reflects the crypto value after accounting for any corporate actions')
    st.dataframe(data)
    st.header('Trend of the Adjusted Closing Price Overall')
    data['Date']=pd.to_datetime(data['Date'])
    fig=px.line(data,x=data['Date'],y=data['Adj Close'])
    st.plotly_chart(fig)