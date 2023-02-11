# import libraries
import streamlit as st
import requests, pandas as pd, numpy as np, datetime as dt, warnings


warnings.filterwarnings("ignore")

st.header("Backtesting analysis")

st.write("The main objective in this backtesting routine is to minimize volatility while realizing some return.")

st.write("""
Trade interval: 5 minutes

Amount: $1000

Assumption: no transaction costs
""")

#####################
# DATA
#####################

st.subheader("Data")

st.write("I use TA-Lib to source the financial data")

start_date1 = dt.datetime(2023,2,7) #yyyy,mm,dd

api_key = 'Q8TjCUYOBw9mIis9s4_tP0UtFZfcXFV2' # Tweleve Data api key

symbol = "BTC/USD"
interval = "5min"
order = "asc" # ascending 

n = 4 
final_df = pd.DataFrame()

for i in range(n):
        i = n-i-1
        end_date = start_date1 - dt.timedelta(days = 15*i)
        start_date = end_date - dt.timedelta(days = 15) # extract 15 days of data 

        # make a for loop to itteratively pull data from Twelve date without having to pay for it.
        api_url = f'https://api.twelvedata.com/time_series?symbol={symbol}&start_date={start_date}&end_date={end_date}&interval={interval}&order={order}&apikey={api_key}'
        data = requests.get(api_url).json()
        data_final = pd.DataFrame(data['values'])
        final_df = pd.concat([final_df, data_final[:-1]], ignore_index = True)

from talib import abstract
integer = CDLENGULFING(final_df) # 0 = no pattern, positive = bullish, negative = bearish
final_df['Engulfing'] = integer



st.subheader("Return analysis")

st.subheader("Risk adjusted analysis (Sharpe ratio)")

st.subheader("Risk analysis")

st.subheader("Volatility")

st.subheader("Value at Risk")

st.subheader("Excess returns")

st.subheader("Confidence interval for one candle")

st.subheader("Maximum downward analysis")