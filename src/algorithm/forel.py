# -*- coding: utf-8 -*-

from scipy.spatial.distance import cdist
import numpy as np
import random

class Forel:
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

    def __init__(self, data, radius):
        self.data = data
        self.radius = radius

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
            if distance <= self.radius:
                same_objects.append(list(row))

        return np.asarray(same_objects)

    """ Удаление даданных объектов из выборки. """
    def remove_objects(self, objects):
        self.data = np.delete(self.data, objects)

    def run(self):
        clustered_objects = []

        while self.clustering_not_finish():
            # Извлекаем случайный элемент из выборки.
            currently_object = self.get_rand_object()

            # Получаем похоже на него объекты (находящиеся на расстоянии менее заданного).
            same_objects = self.get_same_objects(currently_object)

            # Расчитываем центр масс полученного набора похожих объектов.
            if len(same_objects) == 0:
                center_object = currently_object
            else:
                center_object = self.get_mass_center(same_objects)

            # Стабилизируем центр масс.
            while self.distance_objects(currently_object, center_object) > 1:
                currently_object = center_object
                same_objects = self.get_same_objects(currently_object)
                center_object = self.get_mass_center(same_objects)

            # Очищаем кластеризованные объекты из выборки.
            self.remove_objects(same_objects)

            # Записываем кластеризованные объекты в результирующий массив.
            clustered_objects.append(same_objects)
