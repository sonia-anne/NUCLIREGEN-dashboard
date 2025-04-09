import pandas as pd
import plotly.express as px

# Simulated dataset
data = {
    "Age Group (years)": ["0–2", "3–5", "6–8", "9–11", "12–14", "15–17", "18–20", "21–25", "26–30"],
    "Mortality Rate (%)": [5, 10, 20, 30, 35, 20, 7, 2, 1]
}

df = pd.DataFrame(data)

# Create the bar chart using Plotly Express
fig = px.bar(
    df,
    x="Age Group (years)",
    y="Mortality Rate (%)",
    text="Mortality Rate (%)",
    title="📊 Mortality Rate by Age Group in Progeria Patients",
    labels={"Mortality Rate (%)": "Mortality Rate (%)", "Age Group (years)": "Age Group"},
)

# Styling for clarity and aesthetics
fig.update_traces(marker_color='crimson', textposition='outside')
fig.update_layout(
    xaxis_title="Age Group (years)",
    yaxis_title="Mortality Rate (%)",
    font=dict(family="Roboto Mono", size=14),
    plot_bgcolor='white'
)

# Show in local or Streamlit app
fig.show()
