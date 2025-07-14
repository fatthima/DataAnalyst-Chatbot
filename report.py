import streamlit as st

def run_report_generator(df):
    st.subheader("Data Report Summary")

    st.write(" Dataset Shape")
    st.write(df.shape)

    st.write(" Columns")
    st.write(df.columns.tolist())

    st.write("Missing Values")
    st.dataframe(df.isnull().sum())

    st.write(" Descriptive Stats")
    st.dataframe(df.describe())
