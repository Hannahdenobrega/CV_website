from pathlib import Path
import streamlit as st, pandas as pd, numpy as np
import base64 # for gif 
from PIL import Image




# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.swd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic (1).png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Hannah de Nobrega"
PAGE_ICON = ":wave:"
NAME = "Hannah de Nobrega"
DESCRIPTION1 = "Economist | SARB"
DESCRIPTION2 = "Using a data-driven approach to report on inflation-targeting guidance for the South African Monetary Policy Committee"
DESCRIPTION3 = "Ultra marathon trail runner"
EMAIL = "hannah.de.nobrega@gmail.com"
SOCIAL_MEDIA = {
        "LinkedIn": "https://www.linkedin.com/in/hannah-de-nobrega-03506189/",
        "Github": "https://github.com/Hannahdenobrega",
        "Twitter": "https://twitter.com/HannahdeNobrega"
}

st.set_page_config(
        page_title = PAGE_TITLE,
        page_icon = PAGE_ICON
        #page_title = "Multipage App",
        #page_icon = "",
)

# --- LOAD CSS, PDF ---
with open(css_file) as f:
        st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html = True)
with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap = "small")
with col1:
        st.image(profile_pic, width=320)
        #"""### gif from url"""
        #st.markdown("![Alt Text](https://upload.wikimedia.org/wikipedia/commons/a/a4/Mandelbrot_sequence_new.gif)")

with col2:
        st.title(NAME)
        st.subheader(DESCRIPTION1)
        st.caption(DESCRIPTION3)
        st.write(DESCRIPTION2)
        st.download_button(
                label = "📄 Download resume",
                data = PDFbyte,
                file_name = resume_file.name,
                mime = "application/octet-stream"
        )
        st.write("📨", EMAIL)
        
# --- SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()): 
        cols[index].write(f"[{platform}]({link})")

# -- CURRENT WORK POSITION --
st.subheader("**Economist | South African Reserve Bank**")
st.write("Pretoria: 2022 - Present")
st.write(
        """
        Formulate macroeconomic policy recommendations by identifying, analysing, and modelling inflation as a function of interest rates to the Monetary Policy Committee of South Africa 
        
        Build models using statistical machine learning, risk volatility, dynamic stochastic general equilibrium (DSGE), nowcasting, Bayesian, and semi-structural economic frameworks for inflation targeting and price stability
        
        Forge collaborative networks with international banks (eg. Canada, France, and the World Bank)
        """
)

# -- Education --
st.write("#")
st.subheader("PhD Financial Econometrics | 2023 - present")
st.write(
        """
        To assess the distributional impact that monetary policy has on the risk premium component of the cost of capital in the South African banking sector. 
        """
) 

st.write("#")
st.subheader("Masters Economics Financial Econometrics | 2021")
st.write(
        """
        Detecting wealth inequality by distinguishing constraints on financial inclusion within a heterogenous agent model 

        
        Subjects : _Mathematical Statistics, Data Science, Macroeconomics, Econometrics, Advanced Time Series Econometrics, Advanced Macroeconomics, Advanced Microeconomics, Financial Econometrics_
        """
) 



# --- SKILLS ---

st.write("#")
st.subheader("Skills")
st.write("---")
st.write(
        """
        **R** ---

        Time series analysis by state space methods, volatility modelling, copula modelling, scientific machine learning, classification, regression, clustering, dimensionality reduction, model selection, pre-processing, portfolio optimisation, nowcasting, data analytics and visualisation, report automation, Monte Carlo Markov Chain, Bayesian method for time series

        **Python** ---
        
        Scientific machine learning, deep learning, macroeconomic models, semi-structural economic modelling, functional analysis and measure theory, continuous-time heterogeneous agent modelling, Kalman filtering

        **Matlab** --- 
        
        Dynare, Iris, macroeconomic modelling

         **Other** --- 

        Github,
        Eviews,
        Stata,
        Bloomberg terminals,
        Microsoft Office Suite, 
        Cloud computing
        """
) 

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB1
st.write("🖱️", "**Economist | South African Reserve Bank**")
st.write("Pretoria: 2022/03 - Present")
st.write(
        """
        - Formulate macroeconomic policy recommendations by identifying, analysing, and modelling inflation as a function of interest rates to the Monetary Policy Committee of South Africa 
        - Build models using statistical machine learning, risk volatility, dynamic stochastic general equilibrium (DSGE), nowcasting, Bayesian, and semi-structural economic frameworks for inflation targeting and price stability
        - Forge collaborative networks with international banks (eg. Canada, France, and the World Bank)
        """
)

# --- JOB2
st.write("#")
st.write("🖱️", "**Data Analyst Intern | Cognician**")
st.write("Cape Town: 2021/03 - 2021/08")
st.write(
        """
        - Developed automated learning modules for clients}
        - Analyzed reports  using natural language processing (NPR)
        - Reported results and internal metrics in client facing environments
        - Contributed to whitepapers on overall research findings 
        """
)

# --- JOB3
st.write("#")
st.write("🖱️", "**Economics Tutor | Stellenbosch University**")
st.write("Stellenbosch: 2020/01 - 2021/11")
st.write(
        """
        - Ran tutorials on various first-year Economics modules (20-30 students)
        - Compiled test questions, evaluated and graded academic performance
        """
)

# --- JOB4
st.write("#")
st.write("🖱️", "**Marketing Strategist | Covi-ID [Open-Source App Development Collective]**")
st.write("Cape Town: 2019/02 - 2020/02")
st.write(
        """
        - Crafted app roll-out strategies and business-to-business networking 
        - Collaborated with MIT tech specialists and business development teams
        - No large scale adoption before vaccines  
        """
)

# --- JOB5
st.write("#")
st.write("🖱️", "**Manager | Hanks**")
st.write("Stellenbosch: 2019/02 - 2020/02")
st.write(
        """
        - Restructured and rebuilt a previously sub-optimal business
        - Coordinated strategies to establish brand presence and boost profitability
        - Developed and implemented pricing structures and operations systems
        - [75 percent of revenue objective was met in the first three months]  
        """
)

# --- JOB6
st.write("#")
st.write("🖱️️", "**Volunteer | Love Volunteers**")
st.write("Rwanda: 2018/06 - 2018/07")
st.write(
        """
        - Assisted with teaching, helped build a home, and supported agriculture and women’s empowerment
        """
)


# --- EXPERIENCE AND QUALIFICATIONS ---
st.write("#")
st.subheader("Certifications")
st.write("---")
st.write(
        """
        **GPMN**       ||         DSGE, GEES, and GPM models
        
        **IMF**        ||         Nowcasting 
        
        **EABCN**      ||         Nowcasting using machine learning
        
        **Banque de France** ||  Macroeconomic forecasting
        """
) 


