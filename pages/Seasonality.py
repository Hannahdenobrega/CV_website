import streamlit as st
import subprocess
from PIL import Image

st.title('Seasonality')
st.caption("Author: Hannah de Nobrega")
st.caption("Date: Jan 2023")

st.write("Whether in a debate with a colleague, or in my own capacity beginning the preprocessing of a time series, I often find myself revisiting the first principles of time series. Seasonal adjustment is important because it removes the effects of regular, predictable patterns in a time series data, such as monthly or quarterly fluctuations. This allows for more accurate analysis and comparison of the underlying trend and any other non-seasonal patterns in the data. Without seasonal adjustment, identifying and interpreting underlying trends and patterns in data, as well as making accurate comparisons between time periods, can be difficult.")

st.write("In the figure below it is clear that there is an upward trend in the data, however this trend seems very volatile. The volatility occurs in cycles of one year. Thus we can depict that this data series must be adjusted for (or take out)seasonality so that we can analyse the underlying trend of the time series.")

process1 = subprocess.Popen(["Rscript", "code/raw_data_plot.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
image = Image.open('/Users/hannahdenobrega/Documents/FoP_bin/pages/plots/plot_nsa.png')
st.image(image)
st.caption('**Figure 1:** Raw data - not seasonally adjusted')


st.header("Calculations")

st.subheader(" 1. Calculate the seasonal factor") 

st.write("An important measure called the “seasonal factor” is used to calculate the SAAR. The seasonal factor is calculated by taking the unadjusted data (monthly or quarterly) and dividing it by the annual average number (monthly or quarterly).")

# st.write("Say, for example, Trucape yielded 780,000 apple  in a year. The company's total yield in May was 98,000, in June was 82,000, in July was 96,000, and in August was 78,000.")

st.latex(r'''
annualised~average = \frac{mean(value)}{12}
''')

st.latex(r'''
seasonal~factor = \frac{value}{annualised~average}{12}
''')

process3 = subprocess.Popen(["Rscript", "code/seasonal_factort.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result3 = process3.communicate()
image = Image.open('/Users/hannahdenobrega/Documents/FoP_bin/pages/plots/seasonal_factor.png')
st.image(image)
st.caption('**Figure 2:** Seasonal factor')

st.subheader("2. Calculate the seasonally adjusted value by removing the seasonal factor")

st.write("Divide the non-seasonally adjusted value by the seasonal indexes and multiply by 12 - number of months")

st.latex(r'''
seasonally~adjusted~value = \frac{value}{seasonal~factor}12
''')


process4 = subprocess.Popen(["Rscript", "code/seasonally_adjusted.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result4 = process4.communicate()
image = Image.open('/Users/hannahdenobrega/Documents/FoP_bin/pages/plots/plot_seasonally_adjusted.png')
st.image(image)
st.caption('**Figure 3:** Fruit, seasonally adjusted')

st.header("Implications")

