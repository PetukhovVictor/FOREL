import numpy as np
from sklearn.cluster import KMeans as KMeansAlgorithm
import src.utils as utils

class KMeans:
    def __init__(self, data):
        self.data = data
        self.data_listed = None
        self.kmeans_algorithm = None

    def run(self):
        self.data_listed = [list(row) for row in self.data]
        samples = np.array(self.data_listed)
        self.kmeans_algorithm = KMeansAlgorithm(random_state=1).fit(samples)
        self.kmeans_algorithm.predict(samples)

    def plot(self, column_1_number, column_2_number):
        utils.plot(self.data_listed, self.kmeans_algorithm.labels_,
                   column_1_number, column_2_number, title='K-means results visualization')
