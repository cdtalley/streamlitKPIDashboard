import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# Set page title
st.title("Executive Level KPI Dashboard")  # Switched the title back to your original title

# Using a dummy DataFrame in absence of 'data.csv'
df = pd.DataFrame({
    'Test_Results': np.random.choice(['Passed', 'Failed'], size=100),
    'Server': ['Server'+str(i) for i in np.random.choice(range(10), size=100)],
    'Test_Duration': np.random.randint(1, 100, size=100)})

# Preprocessing data
df['Test_Outcome'] = df['Test_Results'].apply(
    lambda x: 'Passed' if 'Passed' in x else 'Failed')
df_passed = df[df['Test_Outcome'] == 'Passed']
df_failed = df[df['Test_Outcome'] == 'Failed']

# Display total counts
st.subheader('Total Passed:')
st.write(len(df_passed))

st.subheader('Total Failed:')
st.write(len(df_failed))

chart_data = pd.DataFrame({'Test_Outcome': ['Passed', 'Failed'], 'Count': [len(df_passed), len(df_failed)]})

chart = alt.Chart(chart_data).mark_bar().encode(
    x='Test_Outcome',
    y='Count',
    color='Test_Outcome'
).properties(
    title='Test Outcome Grand Total'
)

st.altair_chart(chart, use_container_width=True)

means_passed = df_passed.groupby("Server").Test_Duration.mean().reset_index()

chart = alt.Chart(means_passed).mark_bar().encode(
    x='Server',
    y='Test_Duration'
).properties(
    title='Average Passing Test Duration per Server'
)

st.altair_chart(chart, use_container_width=True)

means_failed = df_failed.groupby("Server").Test_Duration.mean().reset_index()

chart = alt.Chart(means_failed).mark_bar().encode(
    x='Server',
    y='Test_Duration'
).properties(
    title='Average Failed Test Duration per Server'
)

st.altair_chart(chart, use_container_width=True)