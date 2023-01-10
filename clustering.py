from sklearn.cluster import KMeans, SpectralClustering, AgglomerativeClustering, BisectingKMeans
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import LocallyLinearEmbedding

from functions import initializeStudent
from student import Student
import matplotlib.pyplot as plt

def classify_student(student_answers):
    # pca = PCA(n_components=30)
    # X = pca.fit_transform(X)
    embedding = LocallyLinearEmbedding(n_components=15)
    X = embedding.fit_transform(X)

    kmeans = BisectingKMeans(n_clusters=2, random_state=700).fit(X)
    pred = kmeans.predict(X)

    return pred



