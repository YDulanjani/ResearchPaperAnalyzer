import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os


FEEDBACK_COLUMN_THREE = "Feedback"
FEEDBACK_CSV = "feedback.csv"


#needful functions
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index = False).encode('utf-8')


st.title("Dashboard")

st.header("Feedback Analysis")
st.subheader("Feedback Data")

if not os.path.exists(FEEDBACK_CSV):
    st.error("Take Some Feedbacks from Users to view the Analytics 🚨")
else:
    #read the data
    feedbacks = pd.read_csv(FEEDBACK_CSV)
    st.dataframe(feedbacks)
    # save the data
    feedback_data = convert_df(pd.read_csv(FEEDBACK_CSV))
    st.download_button(
        label = "Download Feedback Data",
        data = feedback_data,
        file_name = "feedback.csv",
        mime='text/csv',
    )
    #count plot
    sns.set_theme(style="whitegrid", palette="pastel")
    chart_fig = plt.figure(figsize=(5,5))
    sns.countplot(data = feedbacks, x = FEEDBACK_COLUMN_THREE)
    plt.xlabel("Feedback")
    plt.ylabel("Count")
    plt.title("Feedback Distribution")
    st.pyplot(chart_fig)
