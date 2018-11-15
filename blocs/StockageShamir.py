#!/urs/bin/python2.7
# coding: utf-8

import os
from binarytree import tree
from datetime import *
from random import *


hashh = list()

Blockchain = dict(); #Définition du dictionnaire blockchain prinçipal

g = "Je suis le premier block"
Block = "Block"
nombre = "0"



def generatePolynome(secret,degree):
	var = []
	secret = secret
	degree = degree
	var.append(secret)
	for i in xrange(0,degree):
		a = randint(1,1500)
		var.append(a)
	
def Display(self):
	d = degree
	s = secret
	size = len(var)
	exposant,mono = ' ',''
	for i, j in enumerate(var):
		if j == 0:
			continue
		if i < 2:
			expo = ''
		else:
			expo = str(i)
		exposant += "{0: >6s}".format(expo)
		if i == 0:
			m = "{0:d}".format(j)
		else:
			m = " {0:+d}X".format(j)
		mono += "{0: >6s}".format(m)
	print ("\n P(X) = ".join([exposant,mono]))



def computeX(polynome, x):
	temp = 0
	y = 0
	degres  = len(polynome.var)
	for i in range(0,degres):
		temp = pow(x,i)*polynome[i]
		y += temp
	return y



		# on fourni le secret , le degré du polynome (le nombre de personne pour le reconstruire), l'identifiant du noeud ou stocker le secret
def storeSecret(secret, k, id):
	polynome = Polynome(secret,k) # recupere la liste
	node = [] # liste des noeuds, node[0]=value represente (g(0)=value)
	nombreUsers = getNumberOfUsers() #sensé retourné le nombre d'utilisateurs total du réseau
	x=0 # on commence on premier noeud
	while x < nombreUsers:		      node[x] = computeX(i,x)
		node[x] = pow(node[x],1,p) # modulo p
		x=x+1 # on passe au x suivant
		  #On a maintenant notre liste de noeud pour les stocker
		shareSecret(node,nombreUsers)

def shareSecret(node,nombreUsers): #node et
	for noeud in node:
		print "noeud :",noeud



def getNumberOfUsers():
	return 29 #sensé retourné le nombre d'utilisateurs total du réseau

def prime(x):
	if x%2==0:return False
		elif any(x%i==0 for i in xrange(3,int(sqrt(x))+1,2)):return False
	else:
		return True

		# On choisi au hasard notre p, un nombre premier entre secret et l'infini





class Node:
	def __init__(self,data):
		self.left = None
		self.right = None
		data = data

	def insert(self, data):
	# Compare the new value with the parent node
		if data:
		    if data < data:
		        if self.left is None:
		            self.left = Node(data)
		        else:
		            self.left.insert(data)
		    elif data > data:
		        if self.right is None:
		            self.right = Node(data)
		        else:
		            self.right.insert(data)
		else:
		    data = data

def printPostorder(root):

	if root:

		# First recur on left child
		printPostorder(root.left)

		# the recur on right child
		printPostorder(root.right)

		# now print the data of node
		print(root.data),


print "\nPostorder traversal of binary tree is"


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
        print
        print
	time = datetime.now()
	ha = hash(g)
	nonce = randint(1,100)
	#Blockchain["tx_route"] = hashhhh[0]
	Blockchain["time"] = time
	Blockchain["nonce"] = nonce
	Blockchain["hash_precedent"] = ha
        print hashh


def merkletree():
    inc = 0
    for element in hashh:
	    if inc == 0:
		    root = Node(element)
	    else:
		    root.insert(element)
	    inc = inc + 1
    printPostorder(root)

AjouterBlock()
print
print
print Blockchain
print
print


#def ConcaHash():

# Python program to for tree traversals

# A class that represents an individual node in a
# Binary Tree

storeSecret(5,2)
pol.Display()
