import streamlit as st, pandas as pd, numpy as np, yfinance as yf
import plotly.express as px


st.title("What is the Real impact to move from the LIBOR to SOFR")

st.caption("Author: Hannah de Nobrega")
st.caption("Date: 25 Jan 2023")

st.subheader("LIBOR vs SOFR")

st.write("""

Financial institutions utilise LIBOR (London Interbank Offered Rate) and SOFR (Secured Overnight Financing Rate) to estimate the cost of borrowing. SOFR is based on transactions in the Treasury repurchase agreement (repo) market, whereas LIBOR is based on a bank survey. In addition, SOFR is based on transactions backed by US Treasury securities, making it a more secure rate than LIBOR. Due to concerns about the accuracy and reliability of the LIBOR rate, the Federal Reserve has encouraged market participants to utilise SOFR as an alternative.

""")

st.subheader("New territory")

st.write("""

There are several reasons why investors may be struggling to transition to SOFR. One is that there is a lack of historical data and market participants are not as familiar with SOFR as they are with LIBOR. This can make it more difficult for investors to accurately assess the risk of financial instruments tied to SOFR and make appropriate investment decisions.

Another reason is that SOFR is an overnight rate, while LIBOR is a forward-looking rate. This means that SOFR reflects the cost of borrowing for one day, while LIBOR reflects the cost of borrowing for a specific period of time (e.g., 3 months). This difference can make it difficult for investors to compare the two rates and understand how they will impact their investments.

Additionally, the transition from LIBOR to SOFR is a complex process that involves updating contracts, systems, and processes. This can be a significant undertaking for many investors, especially for those with large portfolios of financial instruments tied to LIBOR.

Furthermore, SOFR is an average of the transaction of secured overnight repos, and it is not available during weekends and holidays, this can make it difficult for investors with short-term investments to adjust their portfolio accordingly.

Overall, the transition from LIBOR to SOFR is a significant change for the financial industry, and it will likely take some time for investors to fully adjust to the new benchmark.

1. *Lack of familiarity*: Many market participants have been using LIBOR for decades and may be more comfortable with its methodology and usage. They may need time to adjust to a new benchmark rate and understand how it is used in financial products.

2. *Limited liquidity*: The SOFR market is not as deep and liquid as the LIBOR market, which means that it may be more difficult for investors to find and execute trades based on SOFR.

3. *Complexity of transition*: The transition from LIBOR to SOFR is complex and will require changes to financial products, contracts, and systems. This could be costly and time-consuming for investors and market participants.

4. *Lack of comparability*: SOFR is an overnight rate while LIBOR is a forward-looking term rate. SOFR may not be as useful to price interest rate derivatives and other financial products that require a term rate.

It's worth noting that there is a global effort to phase out the use of LIBOR, and regulators are encouraging the use of SOFR and other risk-free rates as a replacement. Despite these challenges, many market participants are actively working to transition to SOFR and other alternative reference rates to ensure the stability and integrity of the global financial system.

""")

st.subheader("A more robust future?")

st.write("""

SOFR is considered to be a more robust and reliable benchmark interest rate compared to LIBOR (London Interbank Offered Rate) for several reasons:

1. *Transparency*: SOFR is based on actual transactions in the Treasury repo market, which means that it is a more transparent rate than LIBOR. This is because SOFR is based on observable market data, while LIBOR is based on a survey of banks that may be subject to manipulation.

2. *Reduced risk*: SOFR is based on transactions that are collateralized by U.S. Treasury securities, which makes it a risk-free rate. This means that it is not subject to the credit risk of the banks that participate in the LIBOR survey.

3. *Greater potential liquidity*: The Treasury repo market is highly liquid, which means that there is a large number of transactions taking place every day. This provides a more robust and reliable benchmark rate than LIBOR, which is based on a survey of a small number of banks.

4. *Robustness*: SOFR is a overnight rate and is less affected by short-term fluctuations in the market. It is also not subject to the forward-looking assumptions that are inherent in LIBOR.

5. *Less susceptible to manipulation*: SOFR is based on observable market data, which makes it less susceptible to manipulation than LIBOR, which is based on a survey.

Overall, SOFR is considered to be a more reliable benchmark rate because it is based on actual market transactions, is risk-free, and has greater liquidity and robustness than LIBOR. Due to these reasons, it is being encouraged as replacement of LIBOR by regulators globally.

""")

st.subheader("A reluctant transition")

st.write("""

The transition from LIBOR to SOFR has created a classic mismatch of assets and liabilities. Institutions could potentially have to pay more on the liabilities than they are getting from their underlying assets.

Equity investors are especially frustrated by proposals tied to loans with percieved negative consent clauses, which comprise about 30% of the US leveraged loan market. Those clauses require more than half of creditors to actively vote to reject amendments in the span of five business days, in contrast to a typical loan where debtholders must vote yes for an amendment to pass and have longer to review the proposal.

Which makes it easy for some companies to get through. The pace of amendment requests is expected to pick up in the coming months. About 75% of the $1.4 trillion US leveraged loan market still needs to pivot to SOFR, according to JPMorgan data. 

While some of those loans have fallback language that will eventually flip the debt to the new benchmark with the ARRC-recommended adjustments, a large chunk leave room for flexibility, requiring borrowers to negotiate amendments with creditors.

""")

st.subheader("Expected implications")

st.write("""

The transition from LIBOR to SOFR is expected to have several implications for the financial industry:

1. Reduced risk of manipulation: SOFR is based on a larger and more diverse set of transactions, which makes it less susceptible to manipulation than LIBOR. This will increase the transparency and integrity of the benchmark, which is expected to benefit the industry as a whole.

2. Increased accuracy: SOFR is an overnight rate, which means it is more closely tied to the underlying cash market. This makes it a more accurate measure of short-term interest rates than LIBOR, which is a forward-looking rate.

3. Increased volatility: SOFR is an average of the transactions in the repo market, which can be more volatile than the interbank market on which LIBOR is based. This means that the financial products tied to SOFR may be more volatile than those tied to LIBOR.

4. Changes in pricing: The transition to SOFR will change the pricing of financial products based on the spread between LIBOR and a government bond yield. This could result in some products becoming more or less expensive.

5. Increased operational costs: Transitioning to SOFR will require updating systems, processes, and contracts. It will also require financial institutions and market participants to invest in new technology and infrastructure to ensure they can handle the new benchmark.

6. Difficulty to handle short-term investments: SOFR is an average of overnight repos, and it is not available during weekends and holidays. This can make it difficult for investors with short-term investments to adjust their portfolio accordingly.

Overall, the transition from LIBOR to SOFR is expected to have a significant impact on the financial industry, both in terms of increased transparency and accuracy but also increased volatility and operational costs. It will take a significant effort and resources to ensure a smooth transition and mitigate any negative impact on the market.

""")

