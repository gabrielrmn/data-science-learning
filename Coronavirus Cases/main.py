import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data.csv')

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['date'],
    y=df['cases'],
    name='Total Cases',
    line_shape='linear',
    line_color='rgb(255, 51, 153)'
))

fig.update_layout(

    title='<b>Coronavirus Cases until February 2nd</b>',
    title_x=0.25,
    titlefont=dict(
            family='Gravitas One',
            size=22,
            color='rgb(0, 0, 0)',
        ),

    xaxis=dict(
        showline=True,
        showgrid=True,
        showticklabels=True,
        gridcolor='rgb(26, 0, 13)',
        linecolor='rgb(204, 204, 204)',
        linewidth=2,
        ticks='outside',
        tickfont=dict(
            family='Raleway',
            size=14,
            color='rgb(0, 0, 0)',
        ),
    ),

    yaxis=dict(
        showgrid=True,
        gridcolor='rgb(26, 0, 13)',
        zeroline=False,
        showline=False,
        showticklabels=True,
        title='Total Coronavirus Cases',
        tickfont=dict(
            family='Raleway',
            size=14,
            color='rgb(0, 0, 0)',
        ),
        titlefont=dict(
            family='Gravitas One',
            size=12,
            color='rgb(0, 0, 0)',
        ),
    ),

    annotations = [dict(
        x=0.5,
        y=0.0,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.worldometers.info/coronavirus/">\
            worldometer</a>',
        showarrow = False
    )],

    autosize=False,
    plot_bgcolor='black'
)

fig.update_traces(mode='lines+markers')
fig.show()