import streamlit as st
import altair as al
import numpy as np
import pandas as pd
import random

st.set_page_config(
    page_title="app",page_icon="😎",layout="wide"
)

# st.write("Random Value")

st.markdown("<h2 style='text-align: center;'>Random Value</h2>", unsafe_allow_html=True)

chart_data = pd.DataFrame(
    np.random.rand(10, 3),
    columns=["Length","Width","Size"]
)

col1, col2 =st.columns(2)

with col1:
    st.line_chart(chart_data)

st.markdown("<br>", unsafe_allow_html=True)

with col2:
    st.bar_chart(chart_data)


def predict():
    st.toast("New data")

st.button('predict', on_click=predict)

checked = st.checkbox("Click meeee")
st.write(f"Check status:{checked}")