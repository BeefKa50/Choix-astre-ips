import numpy as np
import pandas as pd
from sklearn.cluster import BisectingKMeans
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

from sklearn.manifold import LocallyLinearEmbedding

from functions import initializeStudent
from student import Student


# Find clusters in the input data
def classify_student(X):
    kmeans = BisectingKMeans(n_clusters=3, random_state=10).fit(X)
    pred = kmeans.predict(X)

    return pred

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

answers = PCA(30).fit_transform(answers)

pred = classify_student(answers)

i = 0
class0_x = []
class0_y = []
class1_x = []
class1_y = []
class2_x = []
class2_y = []
nb0 = 0
nb1 = 0
nb2 = 0

for predi in pred:
    if predi == 0:
        class0_x.append(answers[i,0])
        class0_y.append(answers[i, 1])
        nb0 += 1
    if predi == 1:
        class1_x.append(answers[i,0])
        class1_y.append(answers[i, 1])
        nb1 += 1
    if predi == 2:
        class2_x.append(answers[i,0])
        class2_y.append(answers[i, 1])
        nb2 += 1
    i += 1

print(f"Nb class 0 : {nb0}")
print(f"Nb class 1 : {nb1}")
print(f"Nb class 2 : {nb2}")

plt.scatter(class0_x,class0_y)
plt.scatter(class1_x,class1_y)
plt.scatter(class2_x,class2_y)
plt.xlabel("PCA dimension 1")
plt.ylabel("PCA dimension 2")
plt.title("Clustering students (3 clusters) after reducing data dimension to 2D")
plt.show()


