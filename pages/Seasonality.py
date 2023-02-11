import streamlit as st
import subprocess
from PIL import Image

st.title('Seasonality')
st.caption("Author: Hannah de Nobrega")
st.caption("Date: 22 Jan 2023")

st.subheader("I. Introduction")

st.write("Whether in a debate with a colleague, or in my own capacity beginning the preprocessing of a time series, I often find myself revisiting the first principles of time series. Seasonal adjustment is important because it removes the effects of regular, predictable patterns in a time series data, such as monthly or quarterly fluctuations. This allows for more accurate analysis and comparison of the underlying trend and any other non-seasonal patterns in the data. Without seasonal adjustment, identifying and interpreting underlying trends and patterns in data, as well as making accurate comparisons between time periods, can be difficult.")

st.subheader("What are seasonal adjustments?")

st.write("""

Seasonal adjustments are a statistical technique used to remove the effects of regular patterns of variation that occur within a specific time period, such as a month or a quarter, from a time series data. These patterns, known as seasonal patterns, can make it difficult to identify underlying trends and changes in the data. By removing the effects of these patterns, seasonal adjustments allow for a clearer understanding of the underlying trends and changes in the data.

There are several methods used for seasonal adjustments, including moving averages, X11 and X12-ARIMA, and others. These methods work by analyzing the historical data and identifying the seasonal patterns, and then removing or "adjusting" for these patterns in the data. This allows for a better understanding of the underlying trends and changes in the data, as well as improved forecasting accuracy.

It's important to note that seasonal adjustments are different from trend adjustments, which aim to remove the long-term underlying trends in data. Seasonal adjustments are usually performed before trend adjustments in order to remove the effects of regular patterns and to make it easier to identify underlying trends.

""")

st.subheader("Importance of seasonal adjustments in data analysis")

st.write(""" 

Seasonal adjustments are important in data analysis because they allow for a clearer understanding of the underlying trends and changes in the data. Without adjusting for seasonal patterns, it can be difficult to accurately interpret the data and make informed decisions.

One of the main benefits of seasonal adjustments is that it improves forecasting accuracy. By removing the effects of seasonal patterns, seasonal adjustments allow for a better understanding of the underlying trends and changes in the data, which in turn improves the accuracy of forecasting future values. This is particularly important in industries such as retail, where sales can fluctuate significantly due to seasonal patterns such as increased sales during the holiday season.

Additionally, seasonal adjustments are important for comparing data across different seasons or years. Without adjusting for seasonal patterns, comparisons can be misleading and can lead to incorrect conclusions. For example, a company may appear to be performing poorly in a certain quarter because sales are down, but it may be because that quarter is typically a slow sales period for that industry.

Finally, seasonal adjustments are important for identifying underlying changes in the data. Without adjusting for seasonal patterns, it can be difficult to distinguish between changes in the underlying level of the data and fluctuations due to seasonal patterns.

In summary, seasonal adjustments are important in data analysis because they allow for a clearer understanding of the underlying trends and changes in the data, improved forecasting accuracy, accurate data comparison, and identification of underlying changes in the data.

""")

st.subheader("II. What causes seasonal patterns in data")

st.write(""" 

There are many factors that can cause seasonal patterns in data. Some of the most common causes include:

Climate: Seasonal changes in weather can have a significant impact on certain industries, such as agriculture and tourism. For example, sales of sunscreen and beachwear tend to increase during the summer months, while sales of snow shovels and winter clothing tend to increase during the winter months.

Holidays: Many industries experience increased demand during holiday seasons. For example, retailers often experience increased sales during the Christmas and holiday season, and restaurants and hotels may experience increased demand during the summer vacation period.

Economic factors: Seasonal patterns can also be caused by economic factors such as changes in consumer spending habits. For example, some industries may see increased demand during the summer months when people have more disposable income due to the end of the school year or the release of summer bonuses.

Social factors: Social factors such as cultural events, school schedules, and other regular events can also lead to seasonal patterns in data. For example, the back-to-school season may lead to increased demand for clothing, school supplies, and electronics.

Administrative factors: Some industries may also experience seasonal patterns due to administrative factors such as fiscal years, budget cycles, and tax deadlines.

It's worth noting that not all data has seasonal patterns, it can depend on the industry and context of the data. Understanding the underlying causes of seasonal patterns in your data can help you to better interpret and analyze it.

""")

st.write("In the figure below it is clear that there is an upward trend in the data, however this trend seems very volatile. The volatility occurs in cycles of one year. Thus we can depict that this data series must be adjusted for (or take out)seasonality so that we can analyse the underlying trend of the time series.")

process1 = subprocess.Popen(["Rscript", "code/raw_data_plot.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
#image = Image.open('/Users/hannahdenobrega/Documents/FoP_bin/pages/plots/plot_nsa.png')
image = Image.open('../plots/plot_nsa.png')
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


st.write("""

Not seasonally adjusting your data can lead to misinterpretation of the underlying trends and patterns in the data. Seasonal patterns, such as increased sales during the holiday season or decreased sales during the summer, can cause fluctuations in the data that may be mistaken for long-term trends or changes in the underlying level of the data. Without adjusting for these seasonal patterns, it may be difficult to accurately forecast future values or to identify true underlying changes in the data. Additionally, comparing data across different seasons or years may be misleading without adjusting for seasonal patterns.



A. 
B. 


A. Common examples of seasonal patterns in various industries
B. Factors that contribute to seasonal patterns

III. Methods of seasonal adjustment
A. Moving averages
B. X11 and X12-ARIMA
C. Comparison of different methods

IV. Importance of seasonal adjustments in forecasting
A. How seasonal adjustments improve forecasting accuracy
B. Examples of forecasting errors caused by lack of seasonal adjustments

V. Challenges in seasonal adjustments
A. Identifying and accounting for outliers
B. Handling data with irregular or non-existent seasonal patterns
C. Dealing with missing data

VI. Conclusion
A. Recap of key points
B. Importance of considering seasonal adjustments in data analysis
C. Final thoughts and recommendations for practitioners.





""")

