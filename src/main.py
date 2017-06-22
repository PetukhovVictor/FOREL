# -*- coding: utf-8 -*-

from numpy import genfromtxt

from algorithm.forel import Forel
from algorithm.kmeans import KMeans
from sklearn import preprocessing

# Загружаем data-set.
data = genfromtxt('data/cars.csv', delimiter=',', dtype=float, skip_header=True, usecols=(1, 2, 3, 4, 5, 6, 7, 8))

kmeans = KMeans(data)
kmeans.run()
kmeans.plot(column_1_number=0, column_2_number=1)

# Нормируем данные
min_max_scaler = preprocessing.MinMaxScaler()
data = min_max_scaler.fit_transform(data)

forel = Forel(data, radius=0.3)
forel.run()
forel.plot(column_1_number=0, column_2_number=1)
