import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CSP Usage Dashboard", layout="wide")
st.title("Cloud Service Provider Usage Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("combined_csp_data.csv", encoding="utf-8")
    df = df[df["Product Title"].notna() & (df["Product Title"] != "")]
    df["Usage Date"] = pd.to_datetime(df["Usage Date"], format="mixed")
    df["Month"] = df["Usage Date"].dt.to_period("M").dt.to_timestamp()
    df["gpu_hours"] = pd.to_numeric(df["gpu_hours"], errors="coerce").fillna(0)
    df["vcpu_hours"] = pd.to_numeric(df["vcpu_hours"], errors="coerce").fillna(0)

    df["Product Title"] = (
        df["Product Title"]
        .str.replace("\u2122", "", regex=False)
        .str.replace("™", "", regex=False)
        .str.strip()
    )

    product_map = {}
    for title in df["Product Title"].unique():
        clean = title
        for prefix in ["NVIDIA "]:
            clean = clean.replace(prefix, "")
        product_map[title] = clean
    df["Product Clean"] = df["Product Title"].map(product_map)

    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("Filters")

date_min = df["Usage Date"].min().date()
date_max = df["Usage Date"].max().date()
date_range = st.sidebar.date_input(
    "Date Range", value=(date_min, date_max), min_value=date_min, max_value=date_max
)

if isinstance(date_range, tuple) and len(date_range) == 2:
    mask = (df["Usage Date"].dt.date >= date_range[0]) & (
        df["Usage Date"].dt.date <= date_range[1]
    )
    df = df[mask]

cloud_providers = st.sidebar.multiselect(
    "Cloud Provider", sorted(df["Cloud Provider"].unique()), default=sorted(df["Cloud Provider"].unique())
)
df = df[df["Cloud Provider"].isin(cloud_providers)]

products = st.sidebar.multiselect(
    "Product Title", sorted(df["Product Clean"].unique()), default=sorted(df["Product Clean"].unique())
)
df = df[df["Product Clean"].isin(products)]

all_gpu_models = sorted(df["gpu_model"].dropna().unique())
default_gpu_models = [m for m in all_gpu_models if "NVIDIA" in m.upper()]
gpu_models = st.sidebar.multiselect(
    "GPU Model", all_gpu_models, default=default_gpu_models
)
df = df[df["gpu_model"].isin(gpu_models)]

instance_types = st.sidebar.multiselect(
    "Instance Type", sorted(df["Instance Type"].dropna().unique()), default=sorted(df["Instance Type"].dropna().unique())
)
df = df[df["Instance Type"].isin(instance_types)]

all_companies = sorted(df["Company Name"].dropna().unique())
selected_companies = st.sidebar.multiselect("Company Name (leave empty for all)", all_companies)
if selected_companies:
    df = df[df["Company Name"].isin(selected_companies)]

all_countries = sorted(df["Country"].dropna().unique())
selected_countries = st.sidebar.multiselect("Country (leave empty for all)", all_countries)
if selected_countries:
    df = df[df["Country"].isin(selected_countries)]

st.sidebar.markdown(f"**Showing {len(df):,} rows**")

# --- KPI Row ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total GPU Hours", f"{df['gpu_hours'].sum():,.0f}")
col2.metric("Total vCPU Hours", f"{df['vcpu_hours'].sum():,.0f}")
col3.metric("Distinct Companies", f"{df['Company Name'].nunique():,}")
col4.metric("Distinct Countries", f"{df['Country'].nunique():,}")

st.divider()

# --- 1. GPU Hours Over Time by Cloud Provider ---
st.subheader("GPU Hours Over Time by Cloud Provider")
trend_provider = (
    df.groupby(["Month", "Cloud Provider"])["gpu_hours"].sum().reset_index()
)
fig = px.bar(
    trend_provider, x="Month", y="gpu_hours", color="Cloud Provider",
    labels={"gpu_hours": "GPU Hours", "Month": ""},
    barmode="stack", text="gpu_hours"
)
fig.update_traces(texttemplate="%{text:,.0f}", textposition="inside")
fig.update_layout(xaxis_tickformat="%b %Y", hovermode="x unified")
st.plotly_chart(fig, use_container_width=True)

# --- 2. Distinct Customers Over Time by Cloud Provider ---
st.subheader("Distinct Customers Over Time by Cloud Provider")
cust_trend = (
    df.groupby(["Month", "Cloud Provider"])["Company Name"]
    .nunique().reset_index(name="Distinct Companies")
)
fig2 = px.bar(
    cust_trend, x="Month", y="Distinct Companies", color="Cloud Provider",
    labels={"Month": ""},
    barmode="stack", text="Distinct Companies"
)
fig2.update_traces(textposition="inside")
fig2.update_layout(xaxis_tickformat="%b %Y", hovermode="x unified")
st.plotly_chart(fig2, use_container_width=True)

# --- 3. GPU Hours by Instance Type (top N) ---
st.subheader("GPU Hours by Instance Type")
by_instance = (
    df.groupby("Instance Type")["gpu_hours"].sum()
    .sort_values(ascending=False).reset_index()
)
inst_top_n = st.slider("Show top N instance types", 5, min(100, len(by_instance)), 10, key="inst_top")
inst_slice = by_instance.head(inst_top_n).sort_values("gpu_hours", ascending=True)
fig3 = px.bar(
    inst_slice, x="gpu_hours", y="Instance Type", orientation="h",
    labels={"gpu_hours": "GPU Hours", "Instance Type": ""},
    text="gpu_hours", height=max(400, inst_top_n * 35)
)
fig3.update_traces(texttemplate="%{text:,.0f}", textposition="outside")
st.plotly_chart(fig3, use_container_width=True)

# --- 4. GPU Hours by Product (colored by Cloud Provider) ---
st.subheader("GPU Hours by Product")
by_product_cp = (
    df.groupby(["Product Clean", "Cloud Provider"])["gpu_hours"].sum().reset_index()
)
product_order = (
    by_product_cp.groupby("Product Clean")["gpu_hours"].sum()
    .sort_values(ascending=True).index.tolist()
)
fig4 = px.bar(
    by_product_cp, x="gpu_hours", y="Product Clean", orientation="h",
    color="Cloud Provider",
    labels={"gpu_hours": "GPU Hours", "Product Clean": ""},
    barmode="stack", text="gpu_hours",
    category_orders={"Product Clean": product_order}
)
fig4.update_traces(texttemplate="%{text:,.0f}", textposition="inside")
st.plotly_chart(fig4, use_container_width=True)

# --- 5. % Breakdown of GPU Hours by Product within Each Cloud Provider ---
st.subheader("GPU Hours by Product within Each Cloud Provider (%)")
pct_data = (
    df.groupby(["Cloud Provider", "Product Clean"])["gpu_hours"].sum().reset_index()
)
pct_data["pct"] = pct_data.groupby("Cloud Provider")["gpu_hours"].transform(
    lambda x: x / x.sum() * 100
)
fig5 = px.bar(
    pct_data, x="Cloud Provider", y="pct", color="Product Clean",
    labels={"pct": "% of GPU Hours", "Product Clean": "Product"},
    barmode="stack", text="pct"
)
fig5.update_traces(texttemplate="%{text:.1f}%", textposition="inside")
fig5.update_layout(yaxis_ticksuffix="%")
st.plotly_chart(fig5, use_container_width=True)

# --- 6. Distinct Customers by Cloud Provider ---
st.subheader("Distinct Customers by Cloud Provider")
cust_by_cp = (
    df.groupby("Cloud Provider")["Company Name"].nunique()
    .reset_index(name="Distinct Companies")
)
fig6 = px.bar(
    cust_by_cp, x="Cloud Provider", y="Distinct Companies", color="Cloud Provider",
    text="Distinct Companies"
)
fig6.update_traces(textposition="outside")
st.plotly_chart(fig6, use_container_width=True)

# --- 7. Distinct Customers by Cloud Provider and Product ---
st.subheader("Distinct Customers by Cloud Provider and Product")
cust_cp_prod = (
    df.groupby(["Cloud Provider", "Product Clean"])["Company Name"]
    .nunique().reset_index(name="Distinct Companies")
)
fig7 = px.bar(
    cust_cp_prod, x="Cloud Provider", y="Distinct Companies", color="Product Clean",
    labels={"Product Clean": "Product"},
    barmode="stack", text="Distinct Companies"
)
fig7.update_traces(textposition="inside")
st.plotly_chart(fig7, use_container_width=True)

# --- 8. Distinct Customers by GPU Model by Cloud Provider ---
st.subheader("Distinct Customers by GPU Model by Cloud Provider")
cust_gpu = (
    df.groupby(["gpu_model", "Cloud Provider"])["Company Name"]
    .nunique().reset_index(name="Distinct Companies")
)
fig8 = px.bar(
    cust_gpu, x="gpu_model", y="Distinct Companies", color="Cloud Provider",
    labels={"gpu_model": "GPU Model"},
    barmode="stack", text="Distinct Companies"
)
fig8.update_traces(textposition="inside")
st.plotly_chart(fig8, use_container_width=True)

# --- 9. GPU Hours by Customer (top N) ---
st.subheader("GPU Hours by Customer")
by_customer = (
    df.groupby("Company Name")["gpu_hours"].sum()
    .sort_values(ascending=False).reset_index()
)
cust_top_n = st.slider("Show top N companies", 5, min(100, len(by_customer)), 10, key="cust_top")
cust_slice = by_customer.head(cust_top_n).sort_values("gpu_hours", ascending=True)
fig9 = px.bar(
    cust_slice, x="gpu_hours", y="Company Name", orientation="h",
    labels={"gpu_hours": "GPU Hours", "Company Name": ""},
    text="gpu_hours", height=max(400, cust_top_n * 35)
)
fig9.update_traces(texttemplate="%{text:,.0f}", textposition="outside")
st.plotly_chart(fig9, use_container_width=True)
