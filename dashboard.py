import numpy as np
from dash import Dash, dcc, html, Output, Input
import plotly.express as px
import pandas as pd

from functions import initializeStudent
from student import Student

# Our hypothesis for each answer
# Negatives values stands for ASTRE
# Positive values stands for IPS

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

hypothesis_values = list(our_hypothesis.values())

# Function that returns a div html element containing a slider and its label base on the input label name
# and initial value
def create_slider(label, base_value):
    inner_div = []
    html_label = html.Label(str(label),style={"font-family":"Courier New"})
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

# Function that returns the current score for each student in a dictionary like {student_number:score}
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

# ------------ INITIALIZE DASHBOARD ------------
# Import answers from csv file
df = pd.read_csv(r'data\data.csv')

students = []

# Create a list of Student objects
for index, row in df.iterrows():
    student = Student()
    initializeStudent(student, row)
    students.append(student)

# Get the initial answers (with a coefficient originally set to 1 for each question) and make
# a copy of it
answers = np.array([list(s.answersAsArray().values()) for s in students])
answers_init = np.copy(answers)

# Get all the labels (answers name)
labels = list(students[0].answersAsArray().keys())

# Initialize web app
app = Dash(__name__)

# Initialize the global html div element with the page title
div_content = [
    html.H1("Choix ASTRE-IPS", style={'textAlign': 'center',"font-family":"Courier New"}),
]

# Get all slider (one for each answer) to apply a coefficient to each one with the dashboard
inner_div = []
for label, value in our_hypothesis.items():
    div = create_slider(label, value)
    inner_div.append(div)

# Display the sliders in a grid
global_div = html.Div(inner_div,style={"display": "grid", "grid-template-columns": "33% 33% 33%"})
div_content.append(global_div)

result_div = []
result_1_div = []
result_2_div = []
result_3_div = []

# Initialize the list of ASTRE students
result_1_div.append(html.Label("ASTRE",style={"font-family":"Courier New"}))
result_1_div.append(html.Ul(id="ASTRE",style={"list-style-type":"none"}))
result_div.append(html.Div(result_1_div,style={"width":"130px","font": "200 20px/1.5 Helvetica, Verdana, sans-serif"}))

# Initialize the list of IPS students
result_2_div.append(html.Label("IPS",style={"font-family":"Courier New"}))
result_2_div.append(html.Ul(id="IPS",style={"list-style-type":"none"}))
result_div.append(html.Div(result_2_div,style={"width":"130px","font": "200 20px/1.5 Helvetica, Verdana, sans-serif"}))

# Initialize the list of undecided students
result_3_div .append(html.Label("Indécis",style={"font-family":"Courier New"}))
result_3_div .append(html.Ul(id="Indecis",style={"list-style-type":"none"}))
result_div.append(html.Div(result_3_div,style={"width":"130px","font": "200 20px/1.5 Helvetica, Verdana, sans-serif"}))

# Put the lists in a grid
div_content.append(html.Div(result_div,style={"display": "grid", "padding-left":"350px","padding-top":"50px",
                                              "grid-template-columns": "33% 33% 33%"}))

# Initialize the pie chart representing the proportion of students in each speciality
div_content.append(dcc.Graph(id="pie_chart"),)
app.layout = html.Div(div_content, style={"margin": 30})

# Get one input for each slider in order to link it with the callback function
inputs = (Input(l, 'value') for l in labels)

# ------------ UPDATE DASHBOARD ------------
# Callback function called each time a slider value is updating (by grabbing it)
@app.callback(
    Output('ASTRE', 'children'),
    Output('IPS', 'children'),
    Output('Indecis', 'children'),
    Output("pie_chart", "figure"),
    *inputs
)
def update_graph(*slider_values):

    global answers

    # Get the values of all sliders using the inputs
    values_lst = np.array(list(slider_values))

    # Update the coefficient of each answer
    for i in range(0, answers.shape[0]):
        for k in range(0, answers.shape[1]):
            answers[i, k] = answers_init[i, k] * values_lst[k]

    # Calculate score for each student
    scores = compute_score(answers)

    astre_students = []
    ips_students = []
    unknown_students = []
    threshold_max = 2
    threshold_min = -2

    # Determine whether if a student will choose ASTRE or IPS according to its score
    for student, score in scores.items():
        if score < threshold_min:
            astre_students.append(html.Li(student,style={"text-align":"center","border-bottom":"1px solid #ccc"}))
        elif score > threshold_max:
            ips_students.append(html.Li(student,style={"text-align":"center","border-bottom":"1px solid #ccc"}))
        else:
            unknown_students.append(html.Li(student,style={"text-align":"center","border-bottom":"1px solid #ccc"}))

    # Update the pie chart to show the proportion of ASTRE, IPS and Undecided students
    chart_values = {"Spécialité":["ASTRE","IPS","Indécis"],"Nombre d'étudiants":
        [len(astre_students),len(ips_students),len(unknown_students)]}
    df = pd.DataFrame(chart_values)
    fig = px.pie(df, values="Nombre d'étudiants", names="Spécialité",
                 title='Répartition estimée des étudiants entre les options en INFO')

    return astre_students, ips_students, unknown_students,fig


if __name__ == "__main__":
    app.run(debug=True)
