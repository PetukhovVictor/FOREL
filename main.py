from numpy import genfromtxt
from pprint import pprint

my_data = genfromtxt('data.csv', delimiter=';', dtype=None)

pprint(my_data[0][0])
