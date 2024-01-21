import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   path='/data-pre-processing',
                   name="Datenvorverarbeitung")

layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                [
                    html.H2(
                        "Datenvorverarbeitung",
                        className="mt-3",
                    ),
                    html.P(
                        """
                        Für dieses Projekt wurden die folgenden Datensätze von Open Numbers verwendet:
                        """,
                        className="text-left mt-3",
                    ),
                    html.Ul(
                        children=[
                            html.Li(html.A("Gapminder BP Energy", href="https://github.com/open-numbers/ddf--gapminder--bp_energy")),
                            html.Li(html.A("Gapminder CO2 Emission", href="https://github.com/open-numbers/ddf--gapminder--co2_emission")),
                            html.Li(html.A("Gapminder Fastrack", href="https://github.com/open-numbers/ddf--gapminder--fasttrack")),
                            html.Li(html.A("Gapminder World", href="https://github.com/open-numbers/ddf--gapminder--gapminder_world")),
                            html.Li(html.A("Gapminder Life Expectancy", href="https://github.com/open-numbers/ddf--gapminder--life_expectancy")),

                        ]
                    ),
                    html.P(
                        children=[
                            """
                            Die jeweiligen Datensätze bestehen selbst aus mehreren CSV-Dateien. Daher wurden die 
                            Datensätze zunächst individuell selbst zu einem Dataframe zusammengeführt und zwischengespeichert.
                            """,
                            """
                            Anschließend wurden die einzelnen daraus resultierenden Dataframes zu 
                            einem großen Dataframe zusammengeführt. 
                            """,
                            html.Br(),
                            html.Br(),
                            """Man erhält anschließend einen sehr großen Dataframe mit über 700 Features (Spalten) 
                            für viele verschiedenen Länder und für manche Länder bereits ab dem Jahre 1800. Daraus 
                            lässt sich eine sehr große Korrelationsmatrix erstellen, um die Daten auf interessante 
                            Zusammenhänge einfach zu untersuchen. Weiterhin wurden mithilfe von Plotly ausgewählte 
                            interessante Zusammenhänge in einem Linen oder Scatterplot visualisiert.""",
                            """Am interessantesten gestaltete sich der Zusammenhang zwischen der täglichen 
                            Zuckeraufnahme und dem Body Mass Index. Daher wurde dieser in der statischen 
                            Visualisierung vorgestellt."""
                        ],
                        className="mt-3", style={'text-align': 'justify'},
                    ),
                ]
            ),
        ),
    ], className="mb-3"
)