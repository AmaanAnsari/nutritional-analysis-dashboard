import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html


def get_navbar():
    navbar_order = ["Startseite", "Zucker- und Kalorienaufnahme", "BMI Vergleich", "Datenvorverarbeitung"]

    logo = "https://as2.ftcdn.net/v2/jpg/03/14/96/79/1000_F_314967907_3Rg1IhIQkqYgNAU6DWe5hdrXJOmOpmNj.jpg"
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Inspiration für die Linke Seite der Navbar d.h.
                    # Elemente innerhalb dieser html.A Klammern von hier:
                    # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=logo, height="30px")),
                            dbc.Col(dbc.NavbarBrand("Dashboard - DS using Python", className="ms-2")),
                        ],
                        align="center",
                        className="g-0",
                    ),
                    href="./",
                    style={"textDecoration": "none"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Nav(
                                [
                                    dbc.NavItem(dbc.NavLink(page["name"], href=page["path"]))
                                    for page in sorted(dash.page_registry.values(), key=lambda x: navbar_order.index(x["name"]))
                                ],
                                className="ml-auto",
                                navbar=True,
                            )
                        )
                    ],
                    className="ms-auto",
                    align="center",
                ),
            ]
        ),
        color="dark",
        dark=True,

    )
