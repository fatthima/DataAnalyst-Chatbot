import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def run_visualizations(df):
    st.subheader("Data Visualization")

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    if not numeric_cols:
        st.warning("No numeric columns found for visualization.")
        return

    col_to_plot = st.selectbox("Select a numeric column to visualize", numeric_cols)

    fig, ax = plt.subplots()
    sns.histplot(df[col_to_plot], kde=True, ax=ax)
    st.pyplot(fig)

    st.write("Mean Plot of Numeric Columns")
    means = df[numeric_cols].mean()
    fig2, ax2 = plt.subplots()
    sns.barplot(x=means.index, y=means.values, hue=means.index, legend=False, palette="viridis", ax=ax2)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45)
    st.pyplot(fig2)

