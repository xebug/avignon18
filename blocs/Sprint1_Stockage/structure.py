#!/urs/bin/python2.7
# coding: utf-8

import os
from datetime import *
from random import *

hashh = list()
hashhh = list()
hashhhh = list()
Blockchain = dict(); 					#Définition du dictionnaire blockchain prinçipal

g = "Je suis le premier block"
Block = "Block"
nombre = "0"

def AjouterBlock():
	for element in os.listdir('./data'):
		with open("./data/"+ element, "r") as line:
			for my_line in line:
				column = my_line.split(':')
				id_demandeur = column[0]
				id_chauffeur = column[1]
				p_d = column[2]
				p_a = column[3]
				distance = column[4]
				prix = column[5]
				
				mon_hashh = hash(id_demandeur+id_chauffeur+p_d+p_a+distance+prix)
				hashh.append(mon_hashh)
				
	merkletree()
	time = datetime.now()
	ha = hash(g)
	nonce = randint(1,100)
	Blockchain["tx_route"] = hashhhh[0]
	Blockchain["time"] = time
	Blockchain["nonce"] = nonce
	Blockchain["hash_precedent"] = ha

	

def merkletree():
	inc = 0
	for element in hashh:
		if inc % 2 == 0:
			h = element
		else:
			newhash = hash(h+element)
			hashhh.append(newhash)
			
		inc += 1
			
	incr = 0
	for elem in hashhh:
		if incr % 2 == 0:
			h = elem
		else:
			newhash = hash(h+elem)
			hashhhh.append(newhash)
			
		incr += 1
			
	
AjouterBlock()
print Blockchain
