import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("https://github.com/appmarestaing/image_host/blob/main/visited_states.csv?raw=true")

fig= go.Figure(data=go.Choropleth(
    locations=df['code'],
    z = df['number students'].astype(float),
    locationmode = 'USA-states',
    colorscale= 'jet',
    colorbar_title= 'least to most visited states'
))
fig.update_layout(
    geo_scope='usa',
    title_text="map of visited states"
)
fig.show()

