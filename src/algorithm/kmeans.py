import numpy as np
from sklearn.cluster import KMeans as KMeansAlgorithm
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, data):
        self.data = data
        self.data_listed = None
        self.X = None
        self.Y = None
        self.kmeans_algorithm = None

    def run(self):
        self.data_listed = [list(row) for row in self.data]
        samples = np.array(self.data_listed)
        self.kmeans_algorithm = KMeansAlgorithm(random_state=1).fit(samples)
        self.kmeans_algorithm.predict(samples)

    def plot(self, column_1_number, column_2_number):
        self.X = np.array(self.data_listed)[:, column_1_number]
        self.Y = np.array(self.data_listed)[:, column_2_number]
        cs = [self.kmeans_algorithm.labels_[i] for i in range(len(self.kmeans_algorithm.labels_))]
        plt.scatter(self.X, self.Y, c=cs)
        plt.title('K-means results visualization')
        plt.show()
