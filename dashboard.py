import dash
from dash import Dash, html, Input, Output, State, dcc
from dash.dash_table import DataTable
from dash_bootstrap_templates import load_figure_template, ThemeSwitchAIO
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import json
# import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     database="diabetes",
#     user="root",
#     password="root" )

# cursor = conn.cursor()
# cursor.execute("SELECT * FROM diabetes")

# for row in cursor:
#     print(row)

df = pd.read_csv("diabetes.csv", delimiter=",")

app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])

theme_switch = ThemeSwitchAIO(
    aio_id="theme", themes=[dbc.themes.QUARTZ, dbc.themes.VAPOR]
)

graph = html.Div(dcc.Graph(id="theme-switch-graph"), className="m-4")

row_1 = dbc.Row(

)

app.layout = html.Div(
    dbc.Container([theme_switch, graph], className="m-4 dbc"),

)

@app.callback(
    Output("theme-switch-graph", "figure"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_graph_theme(toggle):
    template = "quartz" if toggle else "vapor"
    return px.histogram(df, x="Age", color="Outcome", template=template)


if __name__ == "__main__":
    app.run_server(debug=True)
