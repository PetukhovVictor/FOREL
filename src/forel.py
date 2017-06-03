# -*- coding: utf-8 -*-

import numpy as np
import random

from scipy.spatial.distance import cdist

from pprint import pprint

class Forel:
    """ Радиус сферы, внутри которой объекты являются похожими (одного кластера). """
    RADIUS = 15

    """ Получение центра масс набор объектов (массу каждого считаем равной 1). """
    @staticmethod
    def get_mass_center(objects):
        return sum(objects) / len(objects)

    """ Получение расстояния между двумя объектами в Евклидовом пространстве. """
    @staticmethod
    def distance_objects(object1, object2):
        object1 = np.asarray(tuple(object1)).reshape(1, -1)
        object2 = np.asarray(tuple(object2)).reshape(1, -1)

        return cdist(object1, object2, 'euclidean')[0][0]

    def __init__(self, data):
        self.data = data

    """ Получение и извлечение случайного объекта из выборки. """
    def get_rand_object(self):
        if len(self.data) == 0:
            return None
        index = random.randint(0, len(self.data) - 1)
        rand_object = self.data[index]
        self.data = np.delete(self.data, index, 0)

        return rand_object

    """ Проверка наличия ещё некластеризованных объектов. """
    def clustering_not_finish(self):
        return len(self.data) != 0

    """ Получение похожих объектов. Критерий похожести - расстояние в Евклидовом пространстве. """
    def get_same_objects(self, object):
        same_objects = []
        for row in self.data:
            distance = self.distance_objects(object, row)
            if distance <= self.RADIUS:
                same_objects.append(list(row))

        return np.asarray(same_objects)

    """ Удаление даданных объектов из выборки. """
    def remove_objects(self, objects):
        self.data = np.delete(self.data, objects)
