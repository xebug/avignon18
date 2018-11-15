#! /usr/bin/python

def locationId():
	c = CurrentLocalisation()
	j=0
	while j < 16:
		c = c + "a"
		j = j + 1
	
	while i < 16:  
		c = 31 * c + ord(city[i])
		i = i + 1
	return c

def genNetworkId():
	c = locationId()
	h = getID()
	Id = c + h
	return Id	
genNetworkId()	

