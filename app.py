import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# Title
st.set_page_config(page_title="NUCLIREGEN Dashboard", layout="wide")
st.title("📊 Progeria Mortality Analysis – NUCLIREGEN")

# Dataset
age_groups = ["0–4", "5–8", "9–12", "13–16", "17–20", "21–28"]
mortality_rate = [2, 10, 28, 45, 70, 95]  # Hypothetical data
survival_rate = [100 - x for x in mortality_rate]

df = pd.DataFrame({
    "Age Group (Years)": age_groups,
    "Mortality Rate (%)": mortality_rate,
    "Survival Rate (%)": survival_rate
})

# Plotly Graph
fig = go.Figure()

fig.add_trace(go.Bar(
    x=df["Age Group (Years)"],
    y=df["Mortality Rate (%)"],
    name='Mortality Rate',
    marker_color='crimson',
    hovertemplate='%{y}% mortality at age %{x}'
))

fig.add_trace(go.Bar(
    x=df["Age Group (Years)"],
    y=df["Survival Rate (%)"],
    name='Survival Rate',
    marker_color='mediumseagreen',
    hovertemplate='%{y}% survival at age %{x}'
))

fig.update_layout(
    barmode='stack',
    title='Estimated Mortality and Survival in Progeria by Age Group',
    xaxis_title='Age Group (Years)',
    yaxis_title='Percentage (%)',
    plot_bgcolor='white',
    font=dict(family="Arial", size=14),
    legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5)
)

st.plotly_chart(fig, use_container_width=True)
