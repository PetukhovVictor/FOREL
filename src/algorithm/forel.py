# -*- coding: utf-8 -*-

from scipy.spatial.distance import cdist
import numpy as np
import random
import src.utils as utils

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
        self.result = None
        self.clusters = None

    """ Получение и извлечение случайного объекта из выборки. """
    def get_rand_object(self):
        if len(self.data) == 0:
            return None
        if len(self.data) == 1:
            return self.data
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
        counter = 0
        indexes = []
        for row in self.data:
            distance = self.distance_objects(object, row)
            if distance <= self.radius:
                same_objects.append(list(row))
                indexes.append(counter)
            counter += 1

        return [indexes, np.asarray(same_objects)]

    """ Удаление заданных объектов из выборки. """
    def remove_objects(self, same_object_indexes):
        self.data = np.delete(self.data, same_object_indexes, 0)

    """ Запускаем кластеризацию. """
    def run(self):
        self.clustered_objects = []

        while self.clustering_not_finish():
            # Извлекаем случайный элемент из выборки.
            currently_object = self.get_rand_object()

            # Получаем похоже на него объекты (находящиеся на расстоянии менее заданного).
            same_objects_info = self.get_same_objects(currently_object)
            same_object_indexes = same_objects_info[0]
            same_objects = same_objects_info[1]

            # Расчитываем центр масс полученного набора похожих объектов.
            if len(same_objects) == 0:
                center_object = currently_object
            else:
                center_object = self.get_mass_center(same_objects)

            # Стабилизируем центр масс.
            while self.distance_objects(currently_object, center_object) != 0:
                currently_object = center_object
                same_objects_info = self.get_same_objects(currently_object)
                same_object_indexes = same_objects_info[0]
                same_objects = same_objects_info[1]
                center_object = self.get_mass_center(same_objects)

            # Очищаем кластеризованные объекты из выборки.
            self.remove_objects(same_object_indexes)

            # Записываем кластеризованные объекты в результирующий массив.
            self.clustered_objects.append(same_objects_info[1])

        self.result = []
        self.clusters = []
        for cluster in range(len(self.clustered_objects)):
            for row in self.clustered_objects[cluster]:
                self.result.append(list(row))
                self.clusters.append(cluster)

    def plot(self, column_1_number, column_2_number):
        utils.plot(self.result, self.clusters,
                   column_1_number, column_2_number, title='FOREL results vizualization')
