import pickle
import os
from pathlib import Path
import dash_bootstrap_components as dbc

import dash
from dash import html, dcc, callback, Input, Output, State
import plotly.express as px

from dash_app.components.data_processing import get_data_v2

df = get_data_v2(subset=['body_mass_index_bmi_women_kgperm2', "body_mass_index_bmi_men_kgperm2"])

beschreibung_text = [
    """Die beiden Grafiken zeigen den durchschnittlichen Body-Mass-Index (BMI) für Frauen und Männer in verschiedenen 
    Regionen im Zeitverlauf. Der BMI ist ein Maß für das Körpergewicht im Verhältnis zur Körpergröße und wird in 
    Kilogramm pro Quadratmeter (kg/m²) angegeben.
    """,
    html.Br(),
    html.Br(),
    """
    Auf der y-Achse ist der durchschnittliche BMI von Frauen und Männern in kg/m² aufgetragen. Die x-Achse repräsentiert 
    die Jahre. Die Legende ermöglicht eine Unterscheidung nach Regionen."""
]

# Verwendung von Chat-GPT zur Unterstützung bei der Erstellung der Texte,
# die in den folgenden Variablen definiert sind: beschreibung_text

def get_dropdown_options(df_param, column_name):
    df_dropdown = df_param.copy(deep=True)[['geo', 'name', column_name]].dropna(subset=[column_name])
    df_dropdown = df_dropdown[['geo', 'name']].drop_duplicates().sort_values(by='name')
    df_dropdown.rename(columns={'geo': 'value', 'name': 'label'}, inplace=True)
    df_dropdown['label'].fillna(df_dropdown['value'], inplace=True)

    return df_dropdown


df_dropdown_sugar = get_dropdown_options(df, 'body_mass_index_bmi_women_kgperm2')

dash.register_page(
    __name__,
    path='/bmi-analysis',
    name='BMI Vergleich'
)

layout = html.Div(children=[
    html.H1(children='Dynamische Grafik:'),

])

layout = dbc.Container([
    dbc.Row(
        dbc.Col([
            html.H2(children='Vergleich des BMI zwischen Frauen und Männern', className="mt-3"),
            html.P(children=beschreibung_text, style={'text-align': 'justify'}),
            # html.P("Select countries:"),

            dcc.Dropdown(
                id="dropdown_country2",
                options=df_dropdown_sugar['label'],
                multi=True,
                placeholder="Bitte wähle ein oder mehrere Länder aus, um die entsprechenden Grafiken anzuzeigen.",
                clearable=True,
                value=["Germany"]
            )
        ]
        ), className="mb-4"
    ),
    dbc.Row([

        dbc.Col([
            dcc.Graph(id="graph_women"),
        ]),
        dbc.Col([
            dcc.Graph(id="graph_men"),
        ])
    ], className="mb-4", id="graphs2")
])


@callback([Output("graph_women", "figure"), Output("graph_men", "figure")],
          Input("dropdown_country2", "value"))
def update_line_chart(country):
    if len(country) == 0:
        country = ["Africa (mean)", "America (mean)", "Europe (mean)", "Asia (mean)"]

    df.sort_values(by=['year'], inplace=True)
    mask_country = df['name'].isin(country)

    df_women = df[mask_country].dropna(subset=['body_mass_index_bmi_women_kgperm2'])
    df_men = df[mask_country].dropna(subset=['body_mass_index_bmi_men_kgperm2'])
    df_men = df_men[df_men['year'] < df_women['year'].max() + 1]

    graph_women = px.line(df_women,
                          x="year", y='body_mass_index_bmi_women_kgperm2', color='name', template='simple_white')

    graph_women.update_layout(
        title="⌀ Body Mass Index Frauen von {min} bis {max}".format(min=df_women['year'].min(),
                                                                    max=df_women['year'].max()),
        legend_title="Regionen",
        xaxis_title="Jahr",
        yaxis_title="⌀ Body Mass Index Frauen (in kg/m²)",
    )
    graph_women.update_xaxes(range=[df_women['year'].min() - 1, df_women['year'].max()])
    graph_women.update_traces(hovertemplate=None)
    graph_women.update_layout(hovermode="x unified")

    graph_men = px.line(df_men,
                        x="year", y='body_mass_index_bmi_men_kgperm2', color='name',
                        template='simple_white')

    graph_men.update_layout(
        title="⌀ Body Mass Index Männer von {min} bis {max}".format(min=df_men['year'].min(),
                                                                    max=df_men['year'].max()),
        legend_title="Regionen",
        xaxis_title="Jahr",
        yaxis_title="⌀ Body Mass Index Männer (in kg/m²)",
    )
    graph_men.update_xaxes(range=[df_men['year'].min() - 1, df_men['year'].max()])
    graph_men.update_traces(hovertemplate=None)
    graph_men.update_layout(hovermode="x unified")

    return [graph_women, graph_men]
