import pandas as pd
import plotly.express as px

# Datos simulados (puedes reemplazar con datos reales de PRF o WHO)
data = {
    "Age Group (years)": ["0-2", "3-5", "6-8", "9-11", "12-14", "15-17", "18-20", "21-25", "26-30"],
    "Mortality Rate (%)": [5, 10, 20, 30, 35, 20, 7, 2, 1]
}

df = pd.DataFrame(data)

# Crear gráfico de barras
fig = px.bar(
    df,
    x="Age Group (years)",
    y="Mortality Rate (%)",
    text="Mortality Rate (%)",
    title="MORTALITY RATE BY AGE GROUP IN PROGERIA PATIENTS",
    labels={"Mortality Rate (%)": "Mortality (%)", "Age Group (years)": "Age Group"},
)

# Mejoras visuales para publicación científica
fig.update_traces(marker_color='crimson', textposition='outside')
fig.update_layout(
    uniformtext_minsize=8,
    uniformtext_mode='hide',
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family="Roboto Mono", size=14),
    title_font=dict(size=20, family="Roboto Mono", color="black"),
    yaxis=dict(title='Mortality Rate (%)', gridcolor='lightgray'),
    xaxis=dict(title='Age Group (years)', gridcolor='lightgray')
)

# Mostrar en Streamlit (si deseas integrarlo)
# import streamlit as st
# st.plotly_chart(fig)

fig.show()
