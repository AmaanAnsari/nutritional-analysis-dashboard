import dash
from dash import html
import dash_bootstrap_components as dbc

dash.register_page(__name__,
                   name='Startseite',
                   path='/')

intro_text = [
    """
    Das Verständnis der Rolle von Zucker bei der Gewichtszunahme ist angesichts der weltweit steigenden 
    Übergewichtsraten und der damit verbundenen gesundheitlichen Folgen von entscheidender Bedeutung. Die 
    Lebensmittelpyramide, ein allgemeiner Rahmen für eine gesunde Ernährung, betont die Bedeutung eines mäßigen Verzehrs 
    von zugesetztem Zucker.""",
    html.Br(),
    html.Br(),
    """
    Ein übermäßiger Zuckerkonsum kann jedoch zu einem Energieungleichgewicht führen, bei dem die aus Zucker aufgenommenen 
    Kalorien den Energiebedarf des Körpers übersteigen. Tritt dieses Ungleichgewicht über einen längeren Zeitraum 
    regelmäßig auf, kann dies zu einer Gewichtszunahme führen und das Risiko für die Entwicklung von Fettleibigkeit 
    erhöhen. Der Grund dafür ist, dass zuckerhaltige Lebensmittel oft eine hohe Kaloriendichte haben, aber kein 
    Sättigungsgefühl und keine lang anhaltende Energie liefern. Dies kann dazu führen, dass mehr Kalorien als nötig 
    aufgenommen werden, ohne dass sich ein Sättigungs- oder Glücksgefühl einstellt.
    """
]

grafik_text = [
    """Diese Grafik zeigt den Zusammenhang zwischen dem täglichen Zuckerkonsum und dem durchschnittlichen Body Mass 
    Index (BMI) von Frauen in verschiedenen Ländern. Sie konzentriert sich auf die Frage, ob der Zuckerkonsum zu 
    Übergewicht bzw. Fettleibigkeit beiträgt. Auf der x-Achse ist der durchschnittliche prozentuale Anteil von Zucker 
    in der täglichen Ernährung pro Personen aufgetragen, auf der y-Achse der durchschnittliche BMI von Frauen, 
    gemessen in Kilogramm pro Quadratmeter (kg/m²).
    """,
    html.Br(),
    html.Br(),
    """Das Streudiagramm in der Abbildung zeigt Datenpunkte für verschiedene Länder, wobei jeder Datenpunkt ein 
    bestimmtes Land und die entsprechenden Zuckeraufnahme- und BMI-Werte repräsentiert. Die Farbskala zeigt das 
    Niveau der Nährstoffzufuhr in Kilokalorien pro Person und Tag und reicht von grau (niedrige Zufuhr) über grün, 
    gelb bis rot (hohe Zufuhr). Die hellgraue Trendlinie zeigt den Schwellenwert für Übergewicht, definiert als BMI 
    über 24."""
]

result_text = [
    """
    Bei der Analyse der Grafik wird deutlich, dass mit steigendem Zuckeranteil in der Ernährung der 
    durchschnittliche BMI der Frauen tendenziell ansteigt. Dies deutet auf einen positiven Zusammenhang zwischen 
    Zuckerkonsum und Übergewicht hin. In Ländern mit höherem Zuckerkonsum ist der Anteil der Frauen mit einem BMI 
    über der Übergewichtsschwelle tendenziell höher.
    """,
    html.Br(),
    html.Br(),
    """Die Farbskala gibt einen weiteren Einblick in diesen Zusammenhang: Länder mit einer höheren Kalorienaufnahme 
    pro Person und Tag gehen häufig mit einem höheren Zuckerkonsum einher. Dies deutet darauf hin, dass ein höherer 
    Zuckeranteil in der Ernährung zu einer insgesamt höheren Kalorienaufnahme beitragen kann."""

]

limitations_text = [
    """Es ist wichtig, darauf hinzuweisen, dass diese Visualisierung Daten aus dem Jahr 2000 wiedergibt und andere 
    Faktoren, die zu Übergewicht beitragen können, beispielsweise die allgemeine Ernährung, körperliche Aktivität oder 
    genetische Veranlagungen, nicht berücksichtigt werden.
    """
]

# Verwendung von Chat-GPT zur Unterstützung bei der Erstellung der Texte,
# die in den folgenden Variablen definiert sind: limitations_text, result_text, grafik_text, intro_text

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2(children='Auswirkung der täglichen Zuckerzufuhr in verschiedenen Ländern', className="mt-3"),
            html.H4(children='Einführung', className="mt-3"),
            html.P(children=intro_text, style={'text-align': 'justify'}),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H2(children='Statische Visualisierung', className="mt-3"),
            html.H4(children='Beschreibung', className="mt-3"),
            html.P(children=grafik_text, style={'text-align': 'justify'}),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H4(children='Grafik', className="mt-3"),
            html.Img(src='assets/statische_grafik.png', style={'width': '100%'})
        ]),
    ]),
    dbc.Row([
        dbc.Col([
            html.H4(children='Auswertung', className="mt-3"),
            html.P(children=result_text, style={'text-align': 'justify'}),
        ])
    ]),
    dbc.Row([
        dbc.Col([
            html.H4(children='Einschränkungen', className="mt-3"),
            html.P(children=limitations_text, style={'text-align': 'justify'}),
        ])
    ]),

], className="mb-3")

