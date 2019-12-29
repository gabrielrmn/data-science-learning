import plotly.graph_objects as go
# Load data frame and tidy it.
import pandas as pd 
df = pd.read_csv('data.csv') # Data to be analyzed

fig = go.Figure(data=go.Choropleth(
    locationmode = 'country names', # set of locations match entries in `locations`
    z = df['players'], # Data to be color-coded
    locations=df['country'], # Spatial coordinates
    colorbar_title = "Players per country", # Title of the color bar
    colorscale = 'plotly3', # Color used
    autocolorscale=False,
    reversescale=True, 
    marker_line_color='black', # Color of the line between countries
    marker_line_width=1.0,
))

fig.update_layout( 
    title_text = 'Number of players per each country in CS:GO StarLadder Berlin Major 2019', # Title of the Choropleth Map
    geo=dict(
        showframe=False,
        showcoastlines=True,
        showcountries=True,
        showrivers=True,
        showlakes=True,
        showocean=True,
        projection_type='equirectangular',
        oceancolor = 'rgb(0, 0, 26)'
    ),
    annotations = [dict(
        x=0.5,
        y=0.0,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://vs.com.br/artigo/csgo-brasil-e-russia-sao-os-paises-com-mais-jogadores-no-major-veja-os-classificados">\
            Versus News</a>',
        showarrow = False
    )]
)

fig.show()