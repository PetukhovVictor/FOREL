import numpy as np
import matplotlib.pyplot as plt

def plot(data, labels, column_1_number, column_2_number, title):
    X = np.array(data)[:, column_1_number]
    Y = np.array(data)[:, column_2_number]
    cs = [labels[i] for i in range(len(labels))]
    plt.scatter(X, Y, c=cs, s=50)
    plt.xlim(0)
    plt.ylim(0)
    plt.title(title)
    plt.show()
