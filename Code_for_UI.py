import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Mini Data App Dashboard", layout="wide")   #st.set_page_config is used to configure the appearance and metadata of your Streamlit application
st.title("Mini Data App UI")   #st.title displays title in a large, bold format
file_path = r"GIVE_THE_PATH_OF_THE_OUTPUT_FILE"

df = pd.read_csv(file_path)

if "created_date" in df.columns:
    df["created_date"] = pd.to_datetime(df["created_date"], errors="coerce")

for col in ["owner", "current_stage", "city", "source", "company_clean"]:
    if col in df.columns:
        df[col] = df[col].astype(str)

if "is_sql" in df.columns:
    df["is_sql"] = df["is_sql"].fillna(0).astype(int)

st.sidebar.header("Filters")  #st.sidebar.header displays medium-sized headings that organize controls or filters

stage = st.sidebar.multiselect("Stage", sorted(df["current_stage"].dropna().unique())) if "current_stage" in df.columns else [] 
city = st.sidebar.multiselect("City", sorted(df["city"].dropna().unique())) if "city" in df.columns else []
source = st.sidebar.multiselect("Source", sorted(df["source"].dropna().unique())) if "source" in df.columns else []
company = st.sidebar.multiselect("Company", sorted(df["company_clean"].dropna().unique())) if "company_clean" in df.columns else []
#st.sidebar.multiselect creates a dropdown menu in the sidebar that allows to pick one or many options from a list

show_sql_only = st.sidebar.toggle("Show only SQL leads") #st.sidebar.toggle adds an on/off switch to your sidebar


date_range = None
if "created_date" in df.columns:
    date_range = st.sidebar.date_input("Created Date Range",[df["created_date"].min(), df["created_date"].max()] )
#st.sidebar.date_input adds a calendar-style date picker to sidebar
filtered_df = df.copy()

if stage:
    filtered_df = filtered_df[filtered_df["current_stage"].isin(stage)]
if city:
    filtered_df = filtered_df[filtered_df["city"].isin(city)]
if source:
    filtered_df = filtered_df[filtered_df["source"].isin(source)]
if company:
    filtered_df = filtered_df[filtered_df["company_clean"].isin(company)]
if date_range:
    filtered_df = filtered_df[
        (filtered_df["created_date"] >= pd.to_datetime(date_range[0])) &
        (filtered_df["created_date"] <= pd.to_datetime(date_range[1])) ]
if show_sql_only:
    filtered_df = filtered_df[filtered_df["is_sql"] == 1]

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Leads", filtered_df["email"].nunique() if "email" in filtered_df.columns else 0)
col2.metric("Total Touches", int(filtered_df["total_touches"].sum()) if "total_touches" in filtered_df.columns else 0)
col3.metric("SQL Count", filtered_df[filtered_df["is_sql"] == 1].shape[0] if "is_sql" in filtered_df.columns else 0)
st.subheader("Unified Leads Table")  #st.subheader is used for small headings
st.dataframe(filtered_df,column_config={"created_date": st.column_config.DateColumn("Created Date",format="DD-MM-YYYY")}) #st.dataframe displays data as an interactive table in app



