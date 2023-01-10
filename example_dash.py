import numpy as np
from dash import Dash, dcc, html, Output, Input
import plotly.express as px
import pandas as pd
import math

from functions import initializeStudent
from student import Student

def create_slider(label):
    html_label = html.Label(str(label)),
    html_slider = dcc.Slider(
               min=-5,
               max=5,
               step=0.2,
               value=1,
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
for label in labels:
    html_label, html_slider = create_slider(label)
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