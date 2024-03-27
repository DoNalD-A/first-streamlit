import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

# Page title
st.set_page_config(page_title='Interactive Data Explorer', page_icon='📊')
st.title('📊 Interactive Data Explorer')

st.title("this is the app title")
st.header("this is the header")
st.markdown("this is the markdown")
st.subheader("this isthe subheader")
st.caption("this is the caption")
st.code("x=2021")


st.checkbox('yes')
st.checkbox('no')
st.button("Click")

st.color_picker("Choose eyour favorite color")
