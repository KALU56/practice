import streamlit as st
from app.utils import load_data, plot_boxplot, get_top_regions

# Page setup
st.set_page_config(page_title="📊 Country Metrics Dashboard", layout="wide")
st.title("📊 Country Data Insights Dashboard")

# Dataset selector
datasets = {
    "Benin - Cleaned": "benin-malanville-cleaned.csv",
    "Benin - Raw": "benin-malanville.csv",
    "Sierra Leone - Bumbuna": "sierraleone-bumbuna.csv",
    "Togo - Dapaong (QC)": "togo-dapaong_qc.csv"
}
selected_dataset = st.sidebar.selectbox("📂 Select a dataset", options=list(datasets.keys()))
data = load_data(f"notebooks/data/{datasets[selected_dataset]}")

# Metric selector
numeric_columns = data.select_dtypes(include=["float64", "int64"]).columns.tolist()
selected_metric = st.sidebar.selectbox("📈 Select a numeric metric", options=numeric_columns if numeric_columns else [])

# Country selector (optional)
if "Country" in data.columns:
    selected_countries = st.sidebar.multiselect("🌍 Filter by country", options=data["Country"].unique())
    if selected_countries:
        data = data[data["Country"].isin(selected_countries)]

# Boxplot
if not data.empty and selected_metric:
    st.subheader(f"📦 Boxplot of {selected_metric}")
    st.pyplot(plot_boxplot(data, selected_metric))

# Top regions
if "Region" in data.columns and selected_metric:
    st.subheader(f"🏅 Top Regions by Average {selected_metric}")
    st.dataframe(get_top_regions(data, selected_metric))
