# to run this script type the following into your terminal: streamlit run stock_dash.py
# to to install packages type the following into your terminal: ip3 install --upgrade plotly.express
# import libraries

import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px

# title of your page
st.title("Stock dashboard")

st.caption("Author: Hannah de Nobrega")
st.caption("Date: 20 Jan 2023")



# create a sidebar where people can type the stock/ticker they are looking for
ticker = st.sidebar.text_input('Ticker')
start_date = st.sidebar.date_input('Start date')
end_date = st.sidebar.date_input('End date')

# download the data from yahoo finance
data = yf.download(ticker, start = start_date, end = end_date)

# create a figure
fig = px.line(data, x = data.index, y = data['Adj Close'], title = ticker)
st.plotly_chart(fig)

# create three different tabs containing different information
pricing_data, fundamental_data, news, openai1 = st.tabs(['Pricing data', 'Fundamental data', 'Top 10 news', 'OpenAI ChatGPT'])

with pricing_data:
        st.write('Price movements')
        data2 = data
        data2['% Change'] = data['Adj Close']/data['Adj Close'].shift(1) -1 # lag one
        data2.dropna(inplace = True)
        st.write(data2)
        annual_return = data2['% Change'].mean()*252*100 # multiply by 252 days to make it an annual change from daily data
        st.write('Annual return is', annual_return, '%')
        stdev = np.std(data2['% Change'])*np.sqrt(252)
        st.write('Annualized standard deviation is', stdev*100, '%')
        st.write('Risk adjusted', annual_return/(stdev*100))


# use alpha vantage api to retrieve fundamental data
from alpha_vantage.fundamentaldata import FundamentalData
with fundamental_data:
        key = 'RDYFMH16ROWU7DM5'
        fd = FundamentalData(key, output_format = 'pandas')
        st.subheader('Balance sheet')
        balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
        bs = balance_sheet.T[2:]
        bs.columns = list(balance_sheet.T.iloc[0])
        st.write(bs)
        st.subheader('Income statement')
        income_statement= fd.get_income_statement_annual(ticker)[0]
        is1 = income_statement.T[2:]
        is1.columns = list(income_statement.T.iloc[0])
        st.write(is1)
        st.subheader('Cash flow statement')
        cash_flow = fd.get_cash_flow_annual(ticker)[0]
        cf = cash_flow.T[2:]
        cf.columns = list(cash_flow.T.iloc[0])
        st.write(cf) 
        



with openai1:
        buy_reason, sell_reason, swot_analysis = st.tab(['3 reasons to buy', '3 reasons to sell', 'swot analysis'])

        with buy_reason:
                st.subheader(f'3 reasons to buy {ticker} stock')
                st.write(buy['message'])
        with sell_reason:
                st.subheader(f'3 reasons to sell {ticker} stock')
                st.write(sell['message'])
        with swot_analysis:
                st.subheader(f'swot analysis of {ticker} stock')
                st.write(swot['message'])


from stocknews import StockNews
with news:
        st.header(f'News of {ticker}')
        sn = StockNews(ticker, save_news = False)
        df_news = sn.read_rss()
        for i in range(10):
                st.subheader(f'News {i+1}')
                st.write(df_news['published'][i])
                st.write(df_news['title'][i])
                st.write(df_news['summary'][i])
                title_sentiment = df_news['sentiment_title'][i]
                st.write(f'Title sentiment {title_sentiment}')
                news_sentiment = df_news['sentiment_summary'][i]
                st.write(f'News sentiment {news_sentiment}')



from pyChatGPT import ChatGPT
session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..ClHSYnHjLYz4i2Yv.MZj1hhIVnt1GgoZFwLyu0imnav5Zdx5ZNCgVYqj26rdc15AOK5meMJ4iREwGNteayW70CrP9teOIMmUTZXK4Z3AtCQ6KpK5-BdXd6D2iok8ju93nyVOS-_XNvx0kY61aGpqVf6GZvSlllY-PoTB_x2MndUmJbdHCFgvL2joqkoNAAGMSNu3rzhYWer3hGubm5B3oIDJf5mYeYr4ijXT-BjK87ORWOXLlqiL6m8NqZIojMI0DtWsMpQ5ghqcNFEiIorw7HmF6VoUN_DE0NfNXyQu3juc_F7M3H6Fu3mMe23ICKOBD9TAOm_y80PYUCl3mqMDNQ1Kv_IBRemVKgPSBDjZE-i_mICw4SBWVvD61wwTPgEW2joPlVgvi0Wd6LW8FT9rD8dR8rXGPRAETWWSCT5XlwRTsCFV0VcAXmLq4dBadsd5rBnLepSIi2_UCgluLggX8z1hizXmLgdqMtA5qxTuVw9_2vRYQ3KJ0TpTgyn7_TBAncDHrEsiq0EGdkm7_sV_U0jNtKmop9-yPK5oMqC3YcH5a0EoM26WHtZ1QPz6-pJBc_hnT42NyVMvLbCMbV27RDol4x5m2aFUi_9fsUeFm0aRuDrqBtuDLIXyLskY9aeuZg-RcgEgphmshF_7LEfIGtXESS97u4A3VSe6E28CpeG4-SlHu5XMkK4XhdlBp9hbjdY7rKwjhxG98pnhfEFJCh7Zp4qluazRuOe__rprYIkTHLmrXl77gSgb1uBuYHBuCJY8n5xlSXlwQ46dU5hJD7B58bgQNujCDN2uhTEpR0286qmx6_DjFQMOt2LQ0fFcHnRgXYbG7YqiW6PDiUGAQ1s_JqIgzqFnh3SYjKZ-DL9kv9edJdwmOwetQiranewGRQCvobpIlK4oPdIIFoiJ1jm_73LziuEJjRVPP4KGjGdH3y08dvJw_GnmmrjoF7Y_ZmJ1_TFpbtYgCbAsM5bGMtdI1oRxLix2l4EonDNhu6krCkzvn4f0t_7Vu-Y6P7b7cSZGFydwrVNlgz4EStVU4cKHQmK6V-2cp_03yyjrKFo-0ZRv97gk3rQIT58QlqhtKiuWAdMuKHoHpeNoro_iGewlVTTJocUxbpGiHFCN3jxLtw9RPNmscupYFgtvtFZHO8kpsndKlVvkDQNji4wZjeg0LX0ftNTSCpQSOeCFf04MMPsBxKpooLbTTFQmm2PmJQyTPr07RyMkwkXx1wn1BSZOhAv69ni_LXwEprgW29JTUdIWIedDgpWHX3fe1dp7Kkz1AD5Bifd7gmME5PlDlEk3dy0-jhm-34aubH6avwfrMCtMKzdE3eRae-nYTjxGrVtB2Cat2nah_2JW3vlA_zOx8AO6iUIJEKF_l8fGa4kqDAzvC1Onsje9T9177yaTa6G49s71cSAH-9IvI-nh5IGGhqGVZqqI_HUmIeqmvCioZPdk0fPaM5q2DfkjYF4c7CJbvbXBTWyw-XxesWJ_gvTrZFeS6wmZpUKyRiM-LoYMVv6yMDASoEpjZcD4ncQWLT7KH9yHeWaY2qtSuDIxRpENASW7yMy9kAroQH-msjkNx1qp6GHulpWUx3D35YRiIMpXYzKt7HhIcu96Md7gFSdYHQCdLNiRGm6an3mMn_WRajMKA0TFFcxGOOta0lqueiX8gaXXRudP7YwB1CaUX6jQgxzuXbx4yRf34P5GtXbdyPPR5t4pjyA62AdrZRWofKvdO2ncndM0_EGWC5eTuIiE29JkQLKLnR5G1RyFs3wugyMVSAB4SkvpvdhSiDWmxhqTS_aq-OSbvEjZOSlMkHT7eSsSP4IVwUOdoxVWdCS3sBDG4r4ivI60k2i8ybjnt3MpbmWPkRuHl7gJwJ86EM188n2IVQ6uIEPDmRhTyAB059ykP3o510oci9d5eW-RqCiQMTI_efSPhJSgR5aRA6dSi2GSxuJPX-D3n2Hv59o9Mfe9fWYXTiVfDBVB2dGF9dz51oyYwy6aTc2IkjI93Pka0raQLcj7tYNht1g5jL4hvzTb8Ebb4QuAl5h8niFyH6uKvsvU5qOdk1jEQN7o7EQ8YHf5CkOvjS9yUwYvnAKUPZYYdpQwjXk5thjuWIFjeO7UQRT9-k_kqRAMHK6BO_p4T786A959vznHbQB6zXO7_oehGBH8lWvEJmmAsI3e_vDx1ED6IUW2wrr3xpWoEGjlJ3GLQjH5gOrL5qvVSjRM4iIrhTKgLOlsKN46Hq_vz-MkAizeb8zg2CiiorXCI92U_VaSteMZPSF-s6GXIv3k05Az3yX0lQiQz0vxY-Kq3JFyI30fEu9E.Sc7lHcFcnDYZYYMT5cq6_g"
api2 = ChatGPT(session_token)
buy = api2.send_message(f'3 reasons to buy {ticker} stock')
sell = api2.send_message(f'3 reasons to sell {ticker} stock')
swot = api2.send_message(f'swot analysis of {ticker} stock')
