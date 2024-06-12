import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


# Set page title
st.set_page_config(page_title="Uber Trips Analysis")

# Define function to load data
@st.cache(persist=True)
def load_data():
    data = pd.read_csv("uberdata.csv")
    return data

# Load data
data = load_data()

# Define sidebar
st.sidebar.title("Options")
purpose_filter = st.sidebar.multiselect("Select purpose(s)", data["PURPOSE*"].unique())
category_filter = st.sidebar.multiselect("Select category(s)", data["CATEGORY*"].unique())

# Filter data
filtered_data = data[(data["PURPOSE*"].isin(purpose_filter)) & (data["CATEGORY*"].isin(category_filter))]

# Define main panel
st.title("Uber Trips Analysis")

# Show data
if st.checkbox("Show data"):
    st.write(filtered_data)

# Display summary statistics
st.subheader("Summary Statistics")
st.write(filtered_data.describe())

# Define visualization
chart_data = filtered_data.groupby(["CATEGORY*", "PURPOSE*"]).agg({"MILES*": "mean"}).reset_index()

# Display chart
if not chart_data.empty:
    chart = alt.Chart(chart_data).mark_bar().encode(
        x="PURPOSE*",
        y="MILES*",
        color="CATEGORY*"
    ).properties(
        width=600,
        height=400
    )

    st.subheader("Average Miles by Purpose and Category")
    st.altair_chart(chart)
else:
    st.warning("No data to display.")
purpose_options = data["PURPOSE*"].unique()
category_options = data["CATEGORY*"].unique()

if st.button("Click here to Show Head"):
    st.write(data.head(5))
if st.button("Click here to Show Tail"):
    st.write(data.tail(5))





























st.write(f"Data has {data.shape[0]} rows and {data.shape[1]} columns.")