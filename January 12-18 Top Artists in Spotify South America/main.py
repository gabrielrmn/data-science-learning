import plotly.graph_objects as go
# Load data frame and tidy it.
import pandas as pd 

df = pd.read_csv('data.csv') # Data to be analyzed

for col in df.columns:
    df[col] = df[col].astype(str)

df['text'] = df['country'] + '<br>' +  \
    'Artista: ' + df['singer']

fig = go.Figure(data=go.Choropleth(
    locationmode = 'country names', # set of locations match entries in `locations`
    z = df['streams'].astype(float), # Data to be color-coded
    locations=df['country'], # Spatial coordinates
    colorbar_title = "Streams", # Title of the color bar
    colorscale = 'plotly3', # Color used
    autocolorscale=False,
    text=df['text'],
    reversescale=True, 
    marker_line_color='black', # Color of the line between countries
    marker_line_width=1.0,
))

fig.update_layout( 
    title_text = 'Artistas mais escutados da semana na América do Sul', # Title of the Choropleth Map
    title_x=0.2,
    geo_scope='south america',
    geo=dict(
        showframe=False,
        showcoastlines=True,
        showcountries=True,
        showrivers=True,
        showlakes=True,
        projection_type='equirectangular',
    ),
    annotations = [dict(
        x=0.5,
        y=0.0,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://kworb.net/">\
            Kworb</a>',
        showarrow = False
    )]
)
fig.show()