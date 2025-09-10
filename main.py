import streamlit as st
import plotly.express as px
from backend import get_levels

st.title("ToneTeller")
st.header("I will analyze the tone of your text")

text = st.text_input("Enter text here: ")

if text:
    print(get_levels(text))
