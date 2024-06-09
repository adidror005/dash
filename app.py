from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

app.layout = [
    html.H1(children='Welcome to Trade Mamba', style={'textAlign':'center'}),
    html.H1(children='Youtube Channel'),
    html.H2(children='Interactive Brokers API Videos'),
    html.Iframe(
        src="https://www.youtube.com/embed/videoseries?list=PLCZZtBmmgxn8CFKysCkcl-B1tqRgCCNIX",
        width="60%",
        height="400px",
        style={"border": "none"}
    ),
    html.H2(children='LLM and RAG Videos'),
    html.Iframe(
        src="https://www.youtube.com/embed/videoseries?list=PLCZZtBmmgxn9DjW2Ygg-xGC_z_Tc2U5A8",
        width="60%",
        height="400px",
        style={"border": "none"}
    ),
    html.H1(children='The ultimate trading APP Comming Soon!', style={'textAlign': 'left'}),

    #dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
    #dcc.Graph(id='graph-content')
]

@callback(
    Output('graph-content', 'figure'),
    Input('dropdown-selection', 'value')
)
def update_graph(value):
    dff = df[df.country==value]
    return px.line(dff, x='year', y='pop')

if __name__ == '__main__':
    app.run(debug=True)

"""
    html.Iframe(
        src="https://www.youtube.com/embed/G2wD2scvT8w",
        style={"height": "400px", "width": "100%"}
    )
"""