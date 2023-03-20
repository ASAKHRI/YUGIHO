import dash
from dash import Dash, html, Input, Output, State, dcc
from dash.dash_table import DataTable
from dash_bootstrap_templates import load_figure_template, ThemeSwitchAIO
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import json
import plotly.graph_objects as go
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

df1 = pd.read_csv("df.csv", delimiter=",")

app = Dash(__name__, external_stylesheets=[dbc.themes.QUARTZ])

theme_switch = ThemeSwitchAIO(
    aio_id="theme", themes=[dbc.themes.QUARTZ, dbc.themes.VAPOR]
)

row_1 = dbc.Row([
        dbc.Col(
        html.H1(id="title", children="Dashboard", style={"text-align" : "center"})
        )
    ]
)

row_2 = dbc.Row(
    [
        dbc.Col(dcc.Graph(id="graph2"),width=6),
        dbc.Col(dcc.Graph(id="theme-switch-graph"),width=6),
    ]
)

row_3 = dbc.Row(
    [
        dbc.Col(DataTable(id="datatable",
                columns=[{"name": i, "id": i, "deletable": True, "selectable": True} for i in df1.columns],
                data=df1.to_dict('records'),
                sort_action="native",
                page_size=15,
                style_as_list_view=True,
                style_cell={
                            'height': '15px',
                            # all three widths are needed
                            'minWidth': '180px', 'width': '180px', 'maxWidth': '280px',
                            'whiteSpace': 'normal'
                        },
                style_header={
                            'backgroundColor': 'rgb(50, 50, 50)',
                            'color': 'white'
                            },
                style_data={
                       'backgroundColor': 'rgb(75, 75, 75)',
                        'color': 'white'},
                fixed_columns={'headers': True, 'data': 1},
                style_table={'minWidth': '100%'},
              ),width=12),
    ]
)


app.layout = dbc.Container([
    dbc.Container([theme_switch], className="m-4 dbc"),
    row_1,
    html.Br(),
    html.Br(),
    row_2,
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(
        html.H2(id="title", children="DataTable", style={"text-align" : "center"})
                )
            ]
        ),
    html.Br(),
    row_3
])

@app.callback(
    Output("theme-switch-graph", "figure"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_graph_theme(toggle):
    template = "quartz" if toggle else "vapor"
    return px.pie(df1,names='diabete', template=template)

@app.callback(
    Output("graph2", "figure"),
    Input(ThemeSwitchAIO.ids.switch("theme"), "value"),
)
def update_graph2_theme(toggle):
    template = "quartz" if toggle else "vapor"
    return px.histogram(df1,x='new_bmi',color='diabete', template=template)



if __name__ == "__main__":
    app.run_server(debug=True)
