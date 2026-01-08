import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px  # Light for bar/scatter
import numpy as np
from pathlib import Path

# Base directory for relative data paths
BASE_DIR = Path(__file__).parent

st.set_page_config(layout="wide", page_title="Kenya Cholera Risk Dashboard", page_icon="🌡️")

# Minimal styling
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    h1 { color: #2c3e50; text-align: center; }
    .sidebar .sidebar-content { background-color: #ffffff; padding: 10px; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

st.title("Kenya Cholera Risk Dashboard")
st.markdown("Simplified view of cholera risks in Kenya (2022-2024). Aggregated for efficiency. Since you're in Nairobi, we've highlighted related districts.")

# Load data once with caching
@st.cache_resource
def load_data():
    df = pd.read_csv(BASE_DIR / "kenya_cholera_modeling_table_cleaned.csv")
    df["expected_cases"] = df["cholera_incidence"] * df["population_density"] / 100_000
    # Monthly agg
    df_monthly = df.groupby(["GID_2", "location_clean", "year", "month"]).agg({
        "expected_cases": "sum", "cholera_incidence": "mean",
        "mean_temp_c": "mean", "total_precip_mm": "mean", "mean_rh": "mean"
    }).reset_index()
    # Yearly agg for efficiency
    df_yearly = df_monthly.groupby(["GID_2", "location_clean", "year"]).agg({
        "expected_cases": "sum", "cholera_incidence": "mean",
        "mean_temp_c": "mean", "total_precip_mm": "mean", "mean_rh": "mean"
    }).reset_index()
    return df_monthly, df_yearly

@st.cache_resource
def load_geometry():
    return gpd.read_file(BASE_DIR / "gadm41_KEN_2 (1).geojson")  # Or use cholera geojson if preferred

df_monthly, df_yearly = load_data()
gdf = load_geometry()

# Sidebar: View mode (default yearly)
st.sidebar.header("View Options")
view_mode = st.sidebar.radio("Choose View", ["Yearly (Default)", "Monthly"], index=0,
                             help="Yearly: Faster, aggregated annually. Monthly: Detailed but more data.")

if view_mode == "Yearly (Default)":
    years = sorted(df_yearly["year"].unique())
    selected_year = st.sidebar.selectbox("Select Year", years)
    df_filtered = df_yearly[df_yearly["year"] == selected_year]
    period_text = f"Year {selected_year} (Annual Aggregate)"
    metric_options = ["Total Expected Cases", "Average Incidence (per 100k)"]
else:
    years = sorted(df_monthly["year"].unique())
    months = sorted(df_monthly["month"].unique())
    selected_year = st.sidebar.selectbox("Select Year", years)
    selected_month = st.sidebar.selectbox("Select Month", months)
    df_filtered = df_monthly[(df_monthly["year"] == selected_year) & (df_monthly["month"] == selected_month)]
    period_text = f"{selected_month}/{selected_year}"
    metric_options = ["Expected Cases", "Incidence (per 100k)"]

metric = st.sidebar.radio("Map Metric", metric_options,
                          help="Cases: Summed for yearly. Incidence: Averaged.")

# Pre-merge and cache map data
@st.cache_resource
def prepare_map_data(_df_filtered, _metric):
    value_col = "expected_cases" if "Cases" in _metric else "cholera_incidence"
    gdf_map = gdf.merge(_df_filtered, on="GID_2", how="left").fillna(0)
    return gdf_map, value_col

gdf_map, value_col = prepare_map_data(df_filtered, metric)
legend = metric.replace(" (per 100k)", " per 100,000") if "Incidence" in metric else metric

# Viz 1: Interactive Map
st.header("Cholera Risk Map")
st.markdown(f"Showing {legend.lower()} for {period_text}. Hover for details (Nairobi areas highlighted if present).")
m = folium.Map(location=[-0.0236, 37.9062], zoom_start=6, tiles="cartodbpositron")  # Center on Kenya
folium.Choropleth(
    geo_data=gdf_map, data=gdf_map, columns=["GID_2", value_col],
    key_on="feature.properties.GID_2", fill_color="YlOrRd", fill_opacity=0.7,
    line_opacity=0.2, legend_name=legend, nan_fill_color="lightgrey", highlight=True
).add_to(m)
tooltip_fields = ["NAME_2", value_col]
tooltip_aliases = ["District", legend]
if view_mode != "Yearly (Default)":
    tooltip_fields += ["mean_temp_c", "total_precip_mm", "mean_rh"]
    tooltip_aliases += ["Avg Temp (°C)", "Total Precip (mm)", "Avg Humidity (%)"]
folium.GeoJson(gdf_map, tooltip=folium.GeoJsonTooltip(fields=tooltip_fields, aliases=tooltip_aliases)).add_to(m)
st_folium(m, width=800, height=500)

# Viz 2: Bar Chart - Top 10 Districts
st.header("Top 10 High-Risk Districts")
top_df = df_filtered.sort_values(value_col, ascending=False).head(10)
fig_bar = px.bar(top_df, x="location_clean", y=value_col, title=f"Top Districts by {legend} ({period_text})",
                 labels={"location_clean": "District", value_col: legend}, color=value_col, color_continuous_scale="YlOrRd")
fig_bar.update_layout(width=800, height=400)
st.plotly_chart(fig_bar)

# Viz 3: Time Series for Selected District
st.header("Time Series Trends")
districts = sorted(df_monthly["location_clean"].unique())  # Use monthly for full trends
district = st.selectbox("Select District (Nairobi suggestion: westlands)", districts, index=districts.index("westlands") if "westlands" in districts else 0)
df_ts = df_monthly[df_monthly["location_clean"] == district] if view_mode != "Yearly (Default)" else df_yearly[df_yearly["location_clean"] == district]
df_ts["date"] = pd.to_datetime(df_ts["year"].astype(str) + "-" + df_ts["month"].astype(str) + "-01") if "month" in df_ts.columns else pd.to_datetime(df_ts["year"].astype(str) + "-01-01")
st.line_chart(df_ts.set_index("date")[[ 'expected_cases', 'cholera_incidence', 'mean_temp_c', 'total_precip_mm']])

# Viz 4 (Bonus): Scatter Plot - Incidence vs Precip
st.header("Incidence vs Precipitation Correlation")
fig_scatter = px.scatter(df_filtered, x="total_precip_mm", y="cholera_incidence",
                         size="expected_cases", color="mean_temp_c", hover_name="location_clean",
                         title=f"Scatter: Incidence vs Precip ({period_text})", labels={"cholera_incidence": "Incidence", "total_precip_mm": "Precip (mm)"})
fig_scatter.update_layout(width=800, height=400)
st.plotly_chart(fig_scatter)

# Summary & Download
st.header("Summary")
col1, col2 = st.columns(2)
col1.metric("Total Districts", len(df_filtered))
col2.metric(f"Avg {legend.split()[1] if 'Average' in legend else legend}", f"{df_filtered[value_col].mean():.2f}")
st.download_button("Download Data", df_filtered.to_csv(index=False).encode("utf-8"), "cholera_data.csv")

st.markdown("Notes: Data from 2022-2024. Yearly view sums cases, averages others for speed. Contact for issues.")
