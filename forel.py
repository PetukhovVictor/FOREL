# -*- coding: utf-8 -*-

import numpy as np
import random

from scipy.spatial.distance import cdist

from pprint import pprint

class Forel:
    """ Радиус сферы, внутри которой объекты являются похожими (одного кластера). """
    RADIUS = 10

    """ Срез для измерений кортежа выборки, которые учавствуют в расчетах схожести и центра масс. """
    SLICE_OBJECT = slice(1, 5)

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
        first_object = np.asarray(tuple(object))[self.SLICE_OBJECT].reshape(1, -1)
        for row in self.data:
            second_object = np.asarray(tuple(row))[self.SLICE_OBJECT].reshape(1, -1)
            distance = cdist(first_object, second_object, 'euclidean')
            if distance <= self.RADIUS:
                same_objects.append(row)
        return same_objects

    """ Получение похожих объектов. Критерий похожести - расстояние в Евклидовом пространстве. """
    def get_mass_center(self, objects):

        return None

