import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Kenya Data Explorer", layout="wide")
st.title("📊 Kenya Data Explorer Dashboard")
st.markdown("**By lucky vincent — @lordlucky-254 | Karatina University | Data/AI** — Rainfall vs Maize, KCSE, House Prices, M-Pesa")

@st.cache_data
def load():
    return pd.read_csv("data/kenya_dashboard.csv")
df = load()

with st.sidebar:
    st.header("Filters")
    counties = st.multiselect("County", sorted(df["county"].unique()), default=sorted(df["county"].unique())[:5])
    years = st.slider("Year range", 2018, 2025, (2018, 2025))
    metric = st.selectbox("Main chart metric", ["maize_yield_tonnes_per_ha", "kcse_mean_score", "house_price_ksh", "mpesa_agents"])

filtered = df[(df["county"].isin(counties)) & (df["year"] >= years[0]) & (df["year"] <= years[1])]
c1, c2, c3, c4 = st.columns(4)
c1.metric("Avg Maize Yield (t/ha)", f"{filtered['maize_yield_tonnes_per_ha'].mean():.2f}")
c2.metric("Avg KCSE Mean", f"{filtered['kcse_mean_score'].mean():.2f}")
c3.metric("Avg House Price (KES)", f"{filtered['house_price_ksh'].mean():,.0f}")
c4.metric("Total M-Pesa Agents", f"{filtered['mpesa_agents'].sum():,}")

col1, col2 = st.columns(2)
with col1:
    st.subheader("🌧️ Rainfall vs Maize Yield")
    st.plotly_chart(px.scatter(filtered, x="rainfall_mm", y="maize_yield_tonnes_per_ha", color="county", size="mpesa_agents", hover_data=["year"]), use_container_width=True)
with col2:
    st.subheader(f"📈 {metric} over time")
    st.plotly_chart(px.line(filtered, x="year", y=metric, color="county", markers=True), use_container_width=True)

st.subheader("📋 Filtered Data")
st.dataframe(filtered, use_container_width=True)
st.download_button("Download filtered CSV", filtered.to_csv(index=False), "kenya_filtered.csv", "text/csv")
st.caption("Data: synthetic demo based on realistic Kenya ranges. Replace data/kenya_dashboard.csv with KNBS / World Bank data for production.")
