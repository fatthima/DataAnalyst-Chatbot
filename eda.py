import streamlit as st
import pandas as pd
import io

def run_eda(df):
    st.subheader("Exploratory Data Analysis (EDA)")

    
    st.write(" Dataset Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)

    st.write("Descriptive Statistics")
    st.dataframe(df.describe())

    
    st.write("Column Data Types")
    dtypes_df = pd.DataFrame(df.dtypes, columns=["Data Type"])
    st.dataframe(dtypes_df)

    
    st.write("Missing Values")
    missing_values = df.isnull().sum()
    st.dataframe(missing_values[missing_values > 0].to_frame(name="Missing Count"))
