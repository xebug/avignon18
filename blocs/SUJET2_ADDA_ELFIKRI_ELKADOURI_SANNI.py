# coding: utf-8
import uuid
from random import randint
import math
import hashlib

class Noeud: # Définition de notre classe de Noeud
	

	def __init__(self):
		self.id = "" # ID du noeud qui sera associé à une personne
		self.x = 48.5  # Coordonnées x de la position de la personne 
		self.y = 50.5  # Coordonnées y de la position de la personne 
	
	def getCurrentLocation(self,anonymized=False):
	    #anonymized: si on veut ou non la localisation exacte.
	    #return la localisation actuelle du noeud
	    
	    #latitude = y
	    #longitude = x

	    # On incrémente les deux premiers nombres après la virgule

		if anonymized:
		    # Génération d'un nombre aléatoire
		    r = randint(1,5) / float(100)

		    # Incrémentation du x
		    a, b = math.modf(self.x)
		    x = round((a + r) + b, 4)

		    # Incrémentation du y
		    a, b = math.modf(self.y)
		    y = round((a + r) + b, 4)

		    return (x, y)
		else:
		    return (self.x, self.y)

	def genMyId(self):
		self.id = uuid.uuid4()
		print "ID normal : ", self.id

	def genNetworkId(self):
		self.id = str(self.x)+str(self.y)+str(uuid.uuid4())
		print "ID+localisation : ", self.id

	def hashNomPrenomUuid(self):
		nom = raw_input("Entrez votre nom : ")
		prenom = raw_input("Entrez votre prenom : ")
		final = str(nom)+str(prenom)+str(uuid.uuid4())
		hash_final = hashlib.md5(final)
		print "Hash Nom+Prenom+UUID : ",hash_final.hexdigest()

noeud1 = Noeud()
print "La position du noeud est : ",noeud1.getCurrentLocation()
noeud1.genMyId()
noeud1.genNetworkId()
noeud1.hashNomPrenomUuid()
