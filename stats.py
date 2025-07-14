import streamlit as st
import numpy as np

def run_statistical_analysis(df):
    st.subheader("Statistical Analysis")

    numeric_cols = df.select_dtypes(include=np.number)
    if numeric_cols.empty:
        st.warning("No numeric columns found for statistical analysis.")
        return

    st.write(" Correlation Matrix")
    corr = numeric_cols.corr()
    st.dataframe(corr)


