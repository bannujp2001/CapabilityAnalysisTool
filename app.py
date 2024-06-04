import streamlit as st
import pandas as pd
import numpy as np

st.title('Capability Analysis Tool')

data_input = st.text_area('Enter Process Data', '1, 2, 3, 4, 5, 6, 7, 8, 9, 10')
data = np.array([float(x) for x in data_input.split(',')])

mean = np.mean(data)
sigma = np.std(data)
USL = st.number_input('Enter USL', value=10.0)
LSL = st.number_input('Enter LSL', value=0.0)

Cp = (USL - LSL) / (6 * sigma)
Cpk = min((USL - mean) / (3 * sigma), (mean - LSL) / (3 * sigma))

st.write('Mean:', mean)
st.write('Sigma:', sigma)
st.write('Cp:', Cp)
st.write('Cpk:', Cpk)

st.line_chart(data)
