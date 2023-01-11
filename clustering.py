from sklearn.cluster import BisectingKMeans

from sklearn.manifold import LocallyLinearEmbedding

# Find clusters in the input data
def classify_student(X):
    # pca = PCA(n_components=30)
    # X = pca.fit_transform(X)
    embedding = LocallyLinearEmbedding(n_components=15)
    X = embedding.fit_transform(X)

    kmeans = BisectingKMeans(n_clusters=2, random_state=700).fit(X)
    pred = kmeans.predict(X)

    return pred



