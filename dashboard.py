import numpy as np
from dash import Dash, dcc, html, Output, Input
import plotly.express as px
import pandas as pd
import math
import plotly.graph_objects as go

from functions import initializeStudent
from student import Student

our_hypothesis = {'Ingénieur expert technique': -0.4, 'Ingénieur, homme de culture': 0.4,
                  'Ingénieur chef de projet': 0.0, 'Procédural': -0.6, 'Orienté objet': 0.6, 'Fonctionnel': 0.2,
                  'Web': 3.4, 'Cloud': 0.0, 'Embarqué': -3.0, 'Mobile': 2.0, 'Développement de jeux vidéos': 2.4,
                  'Mathématiques': -1.4, 'Physique-Chimie': -1.8, 'Littérature et Philosophie': 3.6,
                  'Histoire Géographie': 2.0, 'Gestion': 0.4, 'Arts appliqués': 4.2, "Sciences de l'ingenieur": -2.8,
                  'S5 cryptographie': -1.0, 'S5 physique': -1.6, 'S5 anglais': 0.4, 'S5 conduite de projet': 0.6,
                  'S5 droit du travail': 0.2, 'S5 Électronique': -3.4, 'S5 Programmation': 0.0, 'S5 Algorithmique': 0.0,
                  "S5 Technologie de l'internet": 3.6, 'S5 Architecture des ordinateurs': -3.6,
                  'S5 Logique combinatoire et séquentielle': -2.0, 'S5 Introduction aux IHM': 4.0, 'LabView': -2.0,
                  'Excel': 0.4, 'Blender': 3.8, 'Unity': 3.0, 'Figma': 4.6, 'Cisco Packet Tracer': -3.6,
                  'SolidWorks': -0.8, 'AutoCAD': -1.4, 'Imprimante 3D': -0.6, 'Drone': -1.0, 'Casque VR': 1.8,
                  'Carte électronique programmable': -2.0, 'Oscilloscope': -3.2, 'Casque neuronal': 0.0,
                  'Smartphone': 0.0, 'Rien': 0.0, 'K[art]el': 4.0, 'Ensimersion': 3.2, "Ensim'Elec": -2.0,
                  'Enigma': 0.0, "L'Ensimien": 1.8, 'Statue de Mario': 0.4, 'Boîtier pour carte Arduino': -2.0,
                  'Bouton': 1.2, 'Coque de téléphone': 0.0, 'Lecture': 3.0, 'Bricolage': -1.4, 'Sport': 0.0,
                  'Art et dessin': 3.4, 'Jeux vidéos': 0.0, 'Musique': 0.4, 'Musculation': 0.0,
                  'Utilisation de palettes de couleur': 1.8, 'Non utilisation de palettes de couleurs': -0.2,
                  'Démontage du PC': -1.0, 'Réparation par le BIOS': -1.0, 'Consulter un réparateur': 0.2,
                  'Acheter un nouveau PC': 0.4, 'Prépa intégrée': 0.0, 'CPGE ATS': 0.0, 'CPGE PT': -2.6,
                  'CPGE TSI': -3.0, 'CPGE MP': -1.8, 'CPGE MPSI': -1.8, 'CPGE BL': 5.0, 'CPGE PC': -2.2, 'BTS SIO': 0.0,
                  'BTS SN': -0.6, 'DUT Informatique': 1.0, "DUT Métiers du multimédia et de l'internet": 4.2,
                  'L2/L3 Informatique': -0.4, 'M1/M2 Informatique': -0.6, 'Windows': 0.8, 'MacOS': 1.6, 'Linux': -1.2}

#{'Ingénieur expert technique': -0.4, 'Ingénieur, homme de culture': 0.4, 'Ingénieur chef de projet': 0.0, 'Procédural': -0.6, 'Orienté objet': 0.6, 'Fonctionnel': 0.2, 'Web': 3.4, 'Cloud': 0.0, 'Embarqué': -3.0, 'Mobile': 2.0, 'Développement de jeux vidéos': 2.4, 'Mathématiques': -1.4, 'Physique-Chimie': -1.8, 'Littérature et Philosophie': 3.6, 'Histoire Géographie': 2.0, 'Gestion': 0.4, 'Arts appliqués': 4.2, "Sciences de l'ingenieur": -2.8, 'S5 cryptographie': -1.0, 'S5 physique': -1.6, 'S5 anglais': 0.4, 'S5 conduite de projet': 0.6, 'S5 droit du travail': 0.2, 'S5 Électronique': -3.4, 'S5 Programmation': 0.0, 'S5 Algorithmique': 0.0, "S5 Technologie de l'internet": 3.6, 'S5 Architecture des ordinateurs': -3.6, 'S5 Logique combinatoire et séquentielle': -2.0, 'S5 Introduction aux IHM': 4.0, 'LabView': -2.0, 'Excel': 0.4, 'Blender': 3.8, 'Unity': 3.0, 'Figma': 4.6, 'Cisco Packet Tracer': -3.6, 'SolidWorks': -0.8, 'AutoCAD': -1.4, 'Imprimante 3D': -0.6, 'Drone': -1.0, 'Casque VR': 1.8, 'Carte électronique programmable': -2.0, 'Oscilloscope': -3.2, 'Casque neuronal': 0.0, 'Smartphone': 0.0, 'Rien': 0.0, 'K[art]el': 4.0, 'Ensimersion': 3.2, "Ensim'Elec": -2.0, 'Enigma': 0.0, "L'Ensimien": 1.8, 'Statue de Mario': 0.4, 'Boîtier pour carte Arduino': -2.0, 'Bouton': 1.2, 'Coque de téléphone': 0.0, 'Lecture': 3.0, 'Bricolage': -1.4, 'Sport': 0.0, 'Art et dessin': 3.4, 'Jeux vidéos': 0.0, 'Musique': 0.4, 'Musculation': 0.0, 'Utilisation de palettes de couleur': 1.8, 'Non utilisation de palettes de couleurs': -0.2, 'Démontage du PC': -1.0, 'Réparation par le BIOS': -1.0, 'Consulter un réparateur': 0.2, 'Acheter un nouveau PC': 0.4, 'Prépa intégrée': 0.0, 'CPGE ATS': 0.0, 'CPGE PT': -2.6, 'CPGE TSI': -3.0, 'CPGE MP': -1.8, 'CPGE MPSI': -1.8, 'CPGE BL': 5.0, 'CPGE PC': -2.2, 'BTS SIO': 0.0, 'BTS SN': -0.6, 'DUT Informatique': 1.0, "DUT Métiers du multimédia et de l'internet": 4.2, 'L2/L3 Informatique': -0.4, 'M1/M2 Informatique': -0.6, 'Windows': 0.8, 'MacOS': 1.6, 'Linux': -1.2}

hypothesis_values = list(our_hypothesis.values())


def create_slider(label, base_value):
    inner_div = []
    html_label = html.Label(str(label))
    html_slider = dcc.Slider(
        min=-5,
        max=5,
        step=1,
        value=base_value,
        tooltip={"placement": "bottom", "always_visible": True},
        updatemode='drag',
        persistence=True,
        persistence_type='session',  # 'memory' or 'local'
        id=str(label)
    )
    inner_div.append(html_label)
    inner_div.append(html_slider)

    div = html.Div(inner_div)
    return div


def compute_score(answers):
    res = {}
    for i in range(0, answers.shape[0]):
        student_nb = students[i].id
        # res[student_nb] = np.sum(answers[i])
        sum = 0
        for k in range(0, answers.shape[1]):
            sum += answers[i, k]
        res[student_nb] = sum
    return res


df = pd.read_csv(r'data\data.csv')

students = []


for index, row in df.iterrows():
    student = Student()
    initializeStudent(student, row)
    students.append(student)

answers = np.array([list(s.answersAsArray().values()) for s in students])
answers_init = np.copy(answers)
labels = list(students[0].answersAsArray().keys())

# Data source: https://www.ncei.noaa.gov/access/billions/time-series/US
df = pd.read_csv(
    "https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Dash%20Components/Slider/severe-storms.csv")

rangeslider_marks = {0: '$0', 5: '$5 billion', 10: '$10 billion', 15: '$15 billion', 20: '$20 billion',
                     25: '$25 billion', 30: '$30 billion', 35: '$35 billion', 40: '$40 billion'}

app = Dash(__name__)
div_content = [
    html.H1("Choix ASTRE-IPS", style={'textAlign': 'center'}),
]

inner_div = []
for label, value in our_hypothesis.items():
    div = create_slider(label, value)
    inner_div.append(div)

global_div = html.Div(inner_div,style={"display": "grid", "grid-template-columns": "33% 33% 33%"})
div_content.append(global_div)

div_content.append(html.Label("ASTRE"))
div_content.append(html.Ul(id="ASTRE"))
div_content.append(html.Label("IPS"))
div_content.append(html.Ul(id="IPS"))
div_content.append(html.Label("Indécis"))
div_content.append(html.Ul(id="Indecis"))

div_content.append(dcc.Graph(id="pie_chart"),)
app.layout = html.Div(div_content, style={"margin": 30})

inputs = (Input(l, 'value') for l in labels)

@app.callback(
    Output('ASTRE', 'children'),
    Output('IPS', 'children'),
    Output('Indecis', 'children'),
    Output("pie_chart", "figure"),
    *inputs
)
def update_graph(*slider_values):

    global answers

    values_lst = np.array(list(slider_values))

    for i in range(0, answers.shape[0]):
        for k in range(0, answers.shape[1]):
            answers[i, k] = answers_init[i, k] * values_lst[k]

    scores = compute_score(answers)

    astre_students = []
    ips_students = []
    unknown_students = []
    threshold_max = 2
    threshold_min = -2

    for student, score in scores.items():
        if score < threshold_min:
            astre_students.append(html.Li(student))
        elif score > threshold_max:
            ips_students.append(html.Li(student))
        else:
            unknown_students.append(html.Li(student))

    chart_values = {"Spécialité":["ASTRE","IPS","Indécis"],"Nombre d'étudiants":
        [len(astre_students),len(ips_students),len(unknown_students)]}
    df = pd.DataFrame(chart_values)
    fig = px.pie(df, values="Nombre d'étudiants", names="Spécialité",
                 title='Répartition estimée des étudiants entre les options en INFO')

    return astre_students, ips_students, unknown_students,fig


if __name__ == "__main__":
    app.run(debug=True)
