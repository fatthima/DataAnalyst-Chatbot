import streamlit as st
import pandas as pd
from cleaning import clean_data
from eda import run_eda
from visualize import run_visualizations
from stats import run_statistical_analysis
from sql_query import run_sql_queries
from report import run_report_generator

st.set_page_config(page_title="AI Data Analyst Chatbot", layout="wide")

def main():
    st.title("AI Data Analyst Chatbot")

    uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.success("Dataset uploaded successfully.")
        
        df_cleaned = clean_data(df)
        st.success("Data cleaned successfully.")
        
        st.write("Preview of Cleaned Data")
        st.dataframe(df_cleaned)

        options = ["Select", "Exploratory Data Analysis", "Visualization", "Statistical Analysis", "SQL Query", "Report Generator"]
        choice = st.selectbox("Choose the action you want to perform:", options)

        if choice == "Exploratory Data Analysis":
            run_eda(df_cleaned)
        elif choice == "Visualization":
            run_visualizations(df_cleaned)
        elif choice == "Statistical Analysis":
            run_statistical_analysis(df_cleaned)
        elif choice == "SQL Query":
            run_sql_queries(df_cleaned)
        elif choice == "Report Generator":
            run_report_generator(df_cleaned)

if __name__ == '__main__':
    main()


