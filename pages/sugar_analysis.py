import pickle
import os
from pathlib import Path
import dash_bootstrap_components as dbc

import dash
from dash import html, dcc, callback, Input, Output, State
import plotly.express as px

from dash_app.components.data_processing import get_data_v2

df = get_data_v2()

beschreibung_text = [
    """
    Die erste Grafik zeigt die durchschnittliche Zuckeraufnahme pro Person in Gramm über die 
    Jahre. Jede Linie steht für eine Region und zeigt, wie sich die Zuckeraufnahme im Laufe der Zeit verändert hat. Die 
    x-Achse gibt das Jahr an, während die y-Achse die durchschnittliche Zuckeraufnahme pro Person und Tag in Gramm 
    darstellt. Anhand der Legende können die verschiedenen Regionen unterschieden werden. """,
    html.Br(),
    html.Br(),
    """Die zweite Grafik illustriert die durchschnittliche Kalorienaufnahme pro Person und Tag in Kilokalorien über 
    die Jahre. Wie in der ersten Grafik steht jede Linie für eine Region und die x-Achse für das Jahr. Die y-Achse 
    zeigt die durchschnittliche Kalorienaufnahme pro Person und Tag. Auch hier können die verschiedenen Regionen 
    anhand der Legende identifiziert werden."""
]

# Verwendung von Chat-GPT zur Unterstützung bei der Erstellung der Texte,
# die in den folgenden Variablen definiert sind: beschreibung_text

def get_dropdown_options(df_param, column_name):
    df_dropdown = df_param.copy(deep=True)[['geo', 'name', column_name]].dropna(subset=[column_name])
    df_dropdown = df_dropdown[['geo', 'name']].drop_duplicates().sort_values(by='name')
    df_dropdown.rename(columns={'geo': 'value', 'name': 'label'}, inplace=True)
    df_dropdown['label'].fillna(df_dropdown['value'], inplace=True)

    return df_dropdown


df_dropdown_sugar = get_dropdown_options(df, 'sugar_per_person_g_per_day')

dash.register_page(
    __name__,
    path='/sugar-calorie-analysis',
    name='Zucker- und Kalorienaufnahme'
)

layout = html.Div(children=[
    html.H1(children='Dynamische Grafik:'),

])

layout = dbc.Container([
    dbc.Row(
        dbc.Col([
            html.H2(children='Grafiken zur Zucker- und Kalorienaufnahme:', className="mt-3"),
            html.P(children=beschreibung_text, style={'text-align': 'justify'}, className="mb-3"),
            # html.P("Select countries:"),
            dcc.Dropdown(
                id="dropdown_country",
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
            dcc.Graph(id="graph_sugar"),
        ]),
        dbc.Col([
            dcc.Graph(id="graph_calories"),
        ])
    ], className="mb-4", id="graphs")
])


@callback([Output("graph_sugar", "figure"), Output("graph_calories", "figure")],
          Input("dropdown_country", "value"))
def update_line_chart(country):
    if len(country) == 0:
        country = ["Africa (mean)", "America (mean)", "Europe (mean)", "Asia (mean)"]

    df.sort_values(by=['year'], inplace=True)
    mask_country = df['name'].isin(country)

    df_sugar = df[mask_country].dropna(subset=['sugar_per_person_g_per_day'])
    df_calorie = df[mask_country].dropna(subset=['food_supply_kilocalories_per_person_and_day'])
    df_calorie = df_calorie[df_calorie['year'] < df_sugar['year'].max() + 1]

    graph_sugar = px.line(df_sugar,
                          x="year", y='sugar_per_person_g_per_day', color='name', template='simple_white')

    graph_sugar.update_layout(
        title="Tägliche Zuckeraufnahme pro Person von {min} bis {max}".format(min=df_sugar['year'].min(),
                                                                              max=df_sugar['year'].max()),
        legend_title="Regionen",
        xaxis_title="Jahr",
        yaxis_title="⌀ Zuckeraufnahme pro Person pro Tag (in g)"
    )
    graph_sugar.update_xaxes(range=[df_sugar['year'].min() - 1, df_sugar['year'].max()])
    graph_sugar.update_traces(hovertemplate=None)
    graph_sugar.update_layout(hovermode="x unified")

    graph_calories = px.line(df_calorie,
                             x="year", y='food_supply_kilocalories_per_person_and_day', color='name',
                             template='simple_white')

    graph_calories.update_layout(
        title="Tägliche Kalorienaufnahme pro Person von {min} bis {max}".format(min=df_calorie['year'].min(),
                                                                                max=df_calorie['year'].max()),
        legend_title="Regionen",
        xaxis_title="Jahr",
        yaxis_title="⌀ Kalorienaufnahme pro Person pro Tag (in kcal)",
    )
    graph_calories.update_xaxes(range=[df_calorie['year'].min() - 1, df_calorie['year'].max()])
    graph_calories.update_traces(hovertemplate=None)
    graph_calories.update_layout(hovermode="x unified")

    return [graph_sugar, graph_calories]
