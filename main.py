# -*- coding: utf-8 -*-

from numpy import genfromtxt
from pprint import pprint

from forel import Forel

# Загружаем data-set.
data = genfromtxt('data.csv', delimiter=',', dtype=None, skip_header=True)

forel = Forel(data)

while forel.clustering_not_finish():
    # Извлекаем случайный элемент из выборки.
    currently_object = forel.get_rand_object()

    # Получаем похоже на него объекты (находящиеся на расстоянии менее заданного).
    same_objects = forel.get_same_objects(currently_object)

    # Расчитываем центр масс полученного набора похожих объектов.
    center_object = forel.get_mass_center(same_objects)

    pprint(same_objects)
    pprint('----------------------')
