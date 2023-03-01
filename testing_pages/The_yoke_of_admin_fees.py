import streamlit as st
import subprocess
from PIL import Image

st.title('The yoke of admin fees')
st.caption("Author: Hannah de Nobrega")
st.caption("Date: 11 Feb 2023")

st.write("""

In the figure below I illustrate the staggering impact that different scales of management fees have on investors’ overall cumulative returns.

""")

process1 = subprocess.Popen(["Rscript", "code/tyranny_of_fees.R"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
result1 = process1.communicate()
#image = Image.open('/Users/hannahdenobrega/Documents/FoP_bin/pages/plots/plot_tyranny_of_fees.png')
image = Image.open('pages/plots/plot_tyranny_of_fees.png')
st.image(image)
st.caption('''
**Source:** Bloomberg
**Calculations:** Own
''')