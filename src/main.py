# -*- coding: utf-8 -*-

from numpy import genfromtxt

from algorithm.forel import Forel
from algorithm.kmeans import KMeans

# Загружаем data-set.
data = genfromtxt('data/cars.csv', delimiter=',', dtype=None, skip_header=True, usecols=(1, 2, 3, 4))

kmeans = KMeans(data)
kmeans.run()
kmeans.plot(column_1_number=1, column_2_number=2)

# radius - радиус сферы, которой объекты будут считаться похожими (из одного кластера).
forel = Forel(data, radius=15)
forel.run()
forel.plot(column_1_number=1, column_2_number=2)
