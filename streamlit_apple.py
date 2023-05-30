import yfinance as yf
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

st.write('<div align="center"><h3><b>Apple: объём торгов и стоимость акций за 10 лет</b></h3></div>', unsafe_allow_html=True)


apple = yf.Ticker('AAPL')
appledf = apple.history(period='10y', interval = '1d')
appledf = appledf.drop(['Open', 'High', 'Low', 'Dividends', 'Stock Splits'], axis=1).reset_index()
max_stock = appledf['Close'].max()
max_stock_date = appledf.loc[appledf['Close'].idxmax(), 'Date'].date()
min_stock = appledf['Close'].min()  
min_stock_date = appledf.loc[appledf['Close'].idxmin(), 'Date'].date()

chart_width = 1000

plt.figure(figsize=(chart_width / 100, 6))
plt.plot(appledf['Date'], appledf['Close'])
plt.xlabel('Год')
plt.ylabel('Цена акции (долл. США) на закрытии торгов')
st.pyplot(plt)

if st.checkbox('Показать максимальные и минимальные значения стоимости акций **Apple** за 10 лет'):
    st.write('Максимальное значение: {:0.2f} долл. США, дата: {}'.format(max_stock, max_stock_date))
    st.write('Минимальное значение: {:0.2f} долл. США,  дата: {}'.format(min_stock, min_stock_date))

plt.figure(figsize=(chart_width / 100, 6))
plt.plot(appledf['Date'], appledf['Volume'])
plt.xlabel('Год')
plt.ylabel('Объём торгов (шт.)')
plt.ticklabel_format(style='plain', axis='y')
plt.gca().get_yaxis().set_major_formatter(mpl.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
st.pyplot(plt)



