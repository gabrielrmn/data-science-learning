# Crescimento da Populacao Brasileira 1980-2016
# DataSUS
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('populacao-brasileira.csv')

fig = go.Figure()

fig.add_trace(go.Bar(
    x=df['year'],
    y=df['population'],
    showlegend=False,
    marker_color='rgb(26, 118, 255)',
))

fig.add_trace(go.Scatter(
    x=df['year'],
    y=df['population'],
    line_color='rgb(255, 0, 255)',
    showlegend=False
))

fig.update_layout(
    autosize=False,
    width=1920,
    height=640,
    title='Brazilian Population 1980-2016',
    xaxis_tickfont_size=14,
    yaxis=dict(
        title='Population (Millions)',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
)

fig.show()

