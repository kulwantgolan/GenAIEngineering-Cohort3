# BUILDING A SIMPLE STREAMLIT APP - FRONTEND - Streamlit or gradio
import streamlit as st

# Basic Hello World app
st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app!")

if st.button("Click me"):
    st.balloons()

# streamlit run BaseCamp3/Day_2/01_streamlit.py - run on 8501 port by default
