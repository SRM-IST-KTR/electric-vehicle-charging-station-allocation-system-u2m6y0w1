import streamlit as st
from predict_p import show_predict_page
from explore import show_explore_page

page = st.sidebar.selectbox("Predict or explore",("Explore","Predict"))

if page == "Predict":
    show_predict_page()
else:
    show_explore_page()


