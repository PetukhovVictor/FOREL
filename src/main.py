# -*- coding: utf-8 -*-

from pprint import pprint

from numpy import genfromtxt

from algorithm.forel import Forel

# Загружаем data-set.
data = genfromtxt('data/cars.csv', delimiter=',', dtype=None, skip_header=True, usecols=(1, 2, 3, 4))

forel = Forel(data)

clustered_objects = []

while forel.clustering_not_finish():
    # Извлекаем случайный элемент из выборки.
    currently_object = forel.get_rand_object()

    # Получаем похоже на него объекты (находящиеся на расстоянии менее заданного).
    same_objects = forel.get_same_objects(currently_object)

    # Расчитываем центр масс полученного набора похожих объектов.
    if len(same_objects) == 0:
        center_object = currently_object
    else:
        center_object = forel.get_mass_center(same_objects)

    # Стабилизируем центр масс.
    while forel.distance_objects(currently_object, center_object) > 1:
        currently_object = center_object
        same_objects = forel.get_same_objects(currently_object)
        center_object = forel.get_mass_center(same_objects)

    # Очищаем кластеризованные объекты из выборки.
    forel.remove_objects(same_objects)

    # Записываем кластеризованные объекты в результирующий массив.
    clustered_objects.append(same_objects)

pprint(clustered_objects)
