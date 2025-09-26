import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load Data
st.title("CORD-19 COVID-19 Research Papers Explorer")

uploaded_file = st.file_uploader("Upload your CORD-19 CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    # Show basic info
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    # Show dataset shape
    st.write(f"Number of rows: {df.shape[0]}")
    st.write(f"Number of columns: {df.shape[1]}")

    # Example: plot publication years if column exists
    if "publish_time" in df.columns:
        st.subheader("Publications per Year")
        df["Year"] = pd.to_datetime(df["publish_time"], errors="coerce").dt.year
        year_counts = df["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)

    # Example: WordCloud from titles/abstracts
    if "title" in df.columns:
        st.subheader("Word Cloud of Paper Titles")
        text = " ".join(str(t) for t in df["title"].dropna())
        wc = WordCloud(width=800, height=400, background_color="white").generate(text)
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        st.pyplot(plt)
