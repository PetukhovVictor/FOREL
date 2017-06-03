from numpy import genfromtxt
from pprint import pprint


from forel import Forel

data = genfromtxt('data.csv', delimiter=',', dtype=None, skip_header=True)

forel = Forel(data)

while forel.clustering_not_finish():
    currently_object = forel.get_rand_object()
    pprint(currently_object)
