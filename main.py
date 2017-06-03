from numpy import genfromtxt
from pprint import pprint

data = genfromtxt('data.csv', delimiter=',', dtype=None)

pprint(data)
