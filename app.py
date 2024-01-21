import os
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

from dash_app.components.navbar import get_navbar

# os.system("clear")

app = dash.Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc.themes.MORPH]
)

app.layout = app.layout = dbc.Container(
    [
        get_navbar(),
        dbc.Row(
            dbc.Col(
                dash.page_container,
                width={"size": 10, "offset": 1},
                className="bg-light",
            )
        ),
    ],
    fluid=True,
)

if __name__ == "__main__":
    myPort = 8080
    print("Starting server on", myPort)
    app.run_server(debug=False, port=myPort)
