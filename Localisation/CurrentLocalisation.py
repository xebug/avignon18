#! /usr/bin/python
import geocoder
import random

coord = dict()

def CurrentLocalisation(anonymized=True):

	g = geocoder.ip('me')		
	if anonymized == False:
		print(g.latlng)
		return g.latlng,g.city
		
	else:
		l = [random.uniform(0.5, 1.9) for i in range(2)]
		coord[0] = (g.latlng[0]+l[0])
		coord[1] = (g.latlng[1]+l[1])
		print(coord,g.city)
		return coord,g.city


CurrentLocalisation()


