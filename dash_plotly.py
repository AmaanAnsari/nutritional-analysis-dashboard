import os
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

# os.system("clear")

app = dash.Dash(
    __name__,
    use_pages=False,
    external_stylesheets=[dbc.themes.DARKLY],
)

myTopTitle = "Scottish First Baumhaus"
myExternalLink = "https://www.gov.scot/.cloud/"

#############################################################################
###   Navigation bar and side bar
#############################################################################

### Bar on top with title"
myNavbar = dbc.NavbarSimple(
    brand=myTopTitle,
    brand_href=myExternalLink,
    color="primary",
    brand_style={"color": "white", "font-size": "48px"},
)

### Bar on the left hand side
mySidebar = dbc.Nav(
    [
        dbc.NavLink(
            [
                html.Div(page["name"], className="h3 text-white bg-primary p-3"),
            ],
            href=page["path"],
            active="exact",
        )
        for page in dash.page_registry.values()
    ],
    vertical=True,
    pills=True,
    className="page-link bg-light pt-3 pb-3 mt-4",
)

#############################################################################
###   Layout
#############################################################################


app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                myNavbar,
            ),
        ),
        dbc.Row(
            [
                dbc.Col([mySidebar], xs=4, sm=4, md=2, lg=2, xl=2),
                dbc.Col([dash.page_container], xs=8, sm=8, md=10, lg=10, xl=10),
            ],
            className="p-4 mt-2",
        ),
    ],
    fluid=True,
)

#############################################################################
###   Main
#############################################################################


if __name__ == "__main__":
    myPort = 8080
    print("Starting server on", myPort)
    app.run_server(debug=True, port=myPort)
