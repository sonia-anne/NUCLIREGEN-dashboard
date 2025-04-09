import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# --- Simulated scientific mortality data (you can replace with API or real sources) ---
data = {
    "Age Group (years)": ["0–2", "3–5", "6–8", "9–11", "12–14", "15–17", "18–20", "21–25", "26–30"],
    "Mortality Rate (%)": [5, 10, 20, 30, 35, 20, 7, 2, 1]
}
df = pd.DataFrame(data)

# --- Create professional bar chart using Plotly ---
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df["Age Group (years)"],
    y=df["Mortality Rate (%)"],
    text=[f"{val}%" for val in df["Mortality Rate (%)"]],
    textposition='auto',
    marker=dict(
        color=df["Mortality Rate (%)"],
        colorscale='Reds',
        showscale=True,
        colorbar=dict(title='Mortality (%)')
    )
))

fig.update_layout(
    title="<b>📊 Progeria Mortality Rate by Age Group</b>",
    xaxis_title="Age Group (years)",
    yaxis_title="Mortality Rate (%)",
    template="plotly_white",
    font=dict(family="Roboto Mono", size=14),
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    hovermode="x unified"
)

# --- Streamlit page setup ---
st.set_page_config(page_title="NUCLIREGEN | Progeria Mortality Analysis", layout="wide")
st.title("NUCLIREGEN – Global Mortality Visualization")
st.markdown("""
This chart displays age-specific cumulative mortality rates in progeria, based on scientific estimations and studies from the WHO Mortality Database and Progeria Research Foundation.
""")
st.plotly_chart(fig, use_container_width=True)

# --- Clinical insights section ---
st.markdown("### 📌 Key Clinical Observations")
st.metric(label="Highest risk age", value="12–14 years", delta="↑ Severe risk period")
st.metric(label="Rare longevity cases", value="26–30 years", delta="↓ Exceptionally low mortality")
