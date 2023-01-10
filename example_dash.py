import numpy as np
from dash import Dash, dcc, html, Output, Input
import plotly.express as px
import pandas as pd
import math

from functions import initializeStudent
from student import Student

our_hypothesis = {"Ingénieur expert technique":-1,"Ingénieur, homme de culture":1,"Ingénieur chef de projet":0,
              "Procédural":-1,"Orienté objet":1,"Fonctionnel":1,"Web":1,"Cloud":0,"Embarqué":-1,"Mobile":1,
              "Développement de jeux vidéos":1,"Mathématiques":-1,"Physique-Chimie":-1,
              "Littérature et Philosophie":1,"Histoire Géographie":1,"Gestion":0,"Arts appliqués":1,"Sciences de l'ingenieur":-1,
              "S5 cryptographie":-1,"S5 physique":-1,"S5 anglais":1,"S5 conduite de projet":0,"S5 droit du travail":0,
              "S5 Électronique":-1,"S5 Programmation":0,"S5 Algorithmique":0,"S5 Technologie de l'internet":1,
              "S5 Architecture des ordinateurs":-1,"S5 Logique combinatoire et séquentielle":-1,
              "S5 Introduction aux IHM":1,"LabView":-1, "Excel":1, "Blender":1, "Unity":1, "Figma":1,
              "Cisco Packet Tracer":-1, "SolidWorks":-1, "AutoCAD":-1,"Imprimante 3D":-1, "Drone":-1, "Casque VR":1,
              "Carte électronique programmable":-1, "Oscilloscope":-1, "Casque neuronal":0, "Smartphone":0, "Rien":0,
              "K[art]el":1, "Ensimersion":1, "Ensim'Elec":-1, "Enigma":0, "L'Ensimien":1, "Statue de Mario":1,
              "Boîtier pour carte Arduino":-1, "Bouton":-1, "Coque de téléphone":0, "Lecture":1, "Bricolage":-1,
              "Sport":0, "Art et dessin":1, "Jeux vidéos":0, "Musique":0, "Musculation":0,
              "Utilisation de palettes de couleur":1, "Non utilisation de palettes de couleurs":0, "Démontage du PC":-1
              , "Réparation par le BIOS":-1, "Consulter un réparateur":1, "Acheter un nouveau PC":1, "Prépa intégrée":0,
              "CPGE ATS":0, "CPGE PT":-1, "CPGE TSI":-1, "CPGE MP":-1, "CPGE MPSI":-1, "CPGE BL":1, "CPGE PC":-1,
              "BTS SIO":0, "BTS SN":-1, "DUT Informatique":1, "DUT Métiers du multimédia et de l'internet":1,
              "L2/L3 Informatique":0, "M1/M2 Informatique":-1, "Windows":1, "MacOS":1, "Linux":-1}

hypothesis_values = list(our_hypothesis.values())

def create_slider(label,base_value):
    html_label = html.Label(str(label)),
    html_slider = dcc.Slider(
               min=-5,
               max=5,
               step=0.2,
               value=base_value,
               tooltip={"placement": "bottom", "always_visible": True},
               updatemode='drag',
               persistence=True,
               persistence_type='session',  # 'memory' or 'local'
               id=str(label)
               ),
    return html_label, html_slider

def compute_score(answers):
    res = {}
    for i in range(0,answers.shape[0]):
        student_nb = students[i].id
        #res[student_nb] = np.sum(answers[i])
        sum = 0
        for k in range(0,answers.shape[1]):
            sum += answers[i,k]
        res[student_nb] = sum
    return res

df = pd.read_csv(r'data\data.csv')

students = []

for index, row in df.iterrows():
    student = Student()
    initializeStudent(student,row)
    students.append(student)

answers = np.array([list(s.answersAsArray().values()) for s in students])
answers_init = np.copy(answers)
labels = list(students[0].answersAsArray().keys())




# Data source: https://www.ncei.noaa.gov/access/billions/time-series/US
df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Dash%20Components/Slider/severe-storms.csv")

rangeslider_marks = {0:'$0', 5:'$5 billion', 10:'$10 billion', 15:'$15 billion', 20:'$20 billion',
                     25:'$25 billion', 30:'$30 billion', 35:'$35 billion', 40:'$40 billion'}

app = Dash(__name__)
div_content = [
        html.H1("Choix ASTRE-IPS", style={'textAlign': 'center'}),
    ]

for label,value in our_hypothesis.items():
    html_label, html_slider = create_slider(label,value)
    div_content.append(html_label[0])
    div_content.append(html_slider[0])

div_content.append(html.Label("ASTRE"))
div_content.append(html.Ul(id="ASTRE"))
div_content.append(html.Label("IPS"))
div_content.append(html.Ul(id="IPS"))
app.layout = html.Div(div_content,style={"margin": 30})

inputs = (Input(l,'value') for l in labels)
@app.callback(
    Output('ASTRE', 'children'),
    Output('IPS', 'children'),
    *inputs
)

def update_graph(*slider_values):
    global answers
    # bool_series = df['Severe Storm Count'].between(0, n_storms, inclusive='both')
    # df_filtered = df[bool_series]
    # fig = px.bar(data_frame=df_filtered,
    #              x='Year',
    #              y='Severe Storm Count',
    #              range_y=[df['Severe Storm Count'].min(), df['Severe Storm Count'].max()],
    #              range_x=[df['Year'].min()-1, df['Year'].max()+1])
    #
    # bool_series2 = df['Severe Storm Costs (Billions)'].between(dollar_range[0], dollar_range[1], inclusive='both')
    # filtered_year = df[bool_series2]['Year'].values
    # fig["data"][0]["marker"]["color"] = ["orange" if c in filtered_year else "blue" for c in fig["data"][0]["x"]]
    #
    # return fig
    values_lst = np.array(list(slider_values))
    for i in range(0,answers.shape[0]):
        for k in range(0,answers.shape[1]):
            answers[i,k] = answers_init[i,k]*values_lst[k]

    scores = compute_score(answers)

    astre_students = []
    ips_students = []
    for student,score in scores.items():
        if score < 0:
            astre_students.append(html.Li(student))
        if score > 0:
            ips_students.append(html.Li(student))
    return astre_students,ips_students



if __name__ == "__main__":
    app.run(debug=True)