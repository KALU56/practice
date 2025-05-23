import streamlit as st
from app.utils import load_data, plot_boxplot, get_top_regions

st.set_page_config(page_title="📊 Insight Dashboard", layout="wide")
st.title("📊 Insight Dashboard")

# Sidebar widgets
datasets = {
    "Benin Cleaned": "benin-malanville-cleaned.csv",
    "Sierra Leone": "sierraleone-bumbuna.csv",
    "Togo QC": "togo-dapaong_qc.csv"
}

selected_dataset = st.sidebar.selectbox("Select a dataset", list(datasets.keys()))
data = load_data(f"notebooks/data/{datasets[selected_dataset]}")

# Country filter
if "Country" in data.columns:
    countries = data["Country"].unique().tolist()
    selected_countries = st.sidebar.multiselect("Filter by Country", countries)
    if selected_countries:
        data = data[data["Country"].isin(selected_countries)]

# Metric selection
numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns.tolist()
selected_metric = st.sidebar.selectbox("Select a metric to visualize", numeric_columns if numeric_columns else [])

# Visualizations
if not data.empty and selected_metric:
    st.subheader(f"Boxplot: {selected_metric}")
    st.pyplot(plot_boxplot(data, selected_metric))

    if "Region" in data.columns:
        st.subheader(f"Top Regions by {selected_metric}")
        st.dataframe(get_top_regions(data, selected_metric))
