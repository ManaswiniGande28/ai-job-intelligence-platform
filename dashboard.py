import streamlit as st
import pandas as pd

df = pd.read_csv("jobs.csv")

st.title("AI-Powered Job Intelligence Platform")

st.dataframe(df)

st.write("Total Jobs:", len(df))