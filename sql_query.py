import streamlit as st
from pandasql import sqldf

def run_sql_queries(df):
    st.subheader("SQL Query Interface")

    query = st.text_area("Write your SQL query (use 'df' as table name):")
    if st.button("Run Query"):
        try:
            result = sqldf(query, {'df': df})
            st.dataframe(result)
        except Exception as e:
            st.error(f"Error in query: {e}")

