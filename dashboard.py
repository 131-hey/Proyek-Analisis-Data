import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
 
st.title('Bike Sharing Dataset')
tab1, tab2= st.tabs(["Tab 1", "Tab 2"])
 
with tab1:
    st.header("Gathering Data")

    day_df = pd.read_csv("day.csv")
    st.dataframe(day_df.head())
    st.caption('Dengan menggunakan function read_csv() program akan membaca file csv yang kita lampirkan, lalu akan ditampilkan beberapa dengan function head()')


    st.header("Assessing Data")

    st.subheader('Info Data')
    st.write(day_df.info())

 
with tab2:
    st.header("Gathering Data")

    hour_df = pd.read_csv("hour.csv")
    st.dataframe(hour_df.head())
    st.caption('Dengan menggunakan function read_csv() program akan membaca file csv yang kita lampirkan, lalu akan ditampilkan beberapa dengan function head()')

    st.header("Assessing Data")

    st.subheader('Info Data')
    st.write(hour_df.info())




 
