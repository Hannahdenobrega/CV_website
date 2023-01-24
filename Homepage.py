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
DESCRIPTION = """
Economist, assisting the South African Reserve Bank's inflation targeting by supporting data-driven decision-making
"""
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
        st.write(DESCRIPTION)
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

# --- EXPERIENCE AND QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
        """
        - 7 years experionece
        - blah blah
        - blah blah
        """
) 

# --- SKILLS ---

st.write("#")
st.subheader("Skills")
st.write(
        """
        - R
        - Python
        - blah blah
        """
) 

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- JOB1
st.write("📈", "**Economist | South African Reserve Bank**")
st.write("2022/03 - Present")
st.write(
        """
        - Used R and Python to redefine and track commodity price index, exchange rate forecasting and nowcasting. 
        - Led a team of three to brainstorm potential new modeling strategies 
        - Created new relationships with BdF, BoC, and WB  
        """
)

# --- JOB2
st.write("📊", "**Data Analyst Intern | Cognician**")
st.write("2021/03 - 2021/08")
st.write(
        """
        - Used R and Python to redefine and track commodity price index, exchange rate forecasting and nowcasting. 
        - Led a team of three to brainstorm potential new modeling strategies 
        - Created new relationships with BdF, BoC, and WB  
        """
)

# --- JOB3
st.write("📝", "**Economics Tutor | Stellenbosch University**")
st.write("2020/01 - 2021/11")
st.write(
        """
        - Used R and Python to redefine and track commodity price index, exchange rate forecasting and nowcasting. 
        - Led a team of three to brainstorm potential new modeling strategies 
        - Created new relationships with BdF, BoC, and WB  
        """
)

# --- JOB4
st.write("₼", "**Manager | Hanks**")
st.write("2019/02 - 2020/02")
st.write(
        """
        - Used R and Python to redefine and track commodity price index, exchange rate forecasting and nowcasting. 
        - Led a team of three to brainstorm potential new modeling strategies 
        - Created new relationships with BdF, BoC, and WB  
        """
)

# --- JOB5
st.write("📈", "**Volunteer | Love Volunteers**")
st.write("2018/06 - 2018/07")
st.write(
        """
        - Used R and Python to redefine and track commodity price index, exchange rate forecasting and nowcasting. 
        - Led a team of three to brainstorm potential new modeling strategies 
        - Created new relationships with BdF, BoC, and WB  
        """
)



