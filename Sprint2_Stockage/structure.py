#!/urs/bin/python2.7
# coding: utf-8

import os
from binarytree import tree
from datetime import *
from random import *


hashh = list()
hashhh = list()
hashhhh = list()
Blockchain = dict(); #Définition du dictionnaire blockchain prinçipal

g = "Je suis le premier block"
Block = "Block"
nombre = "0"

class Node: 
	def __init__(self,data): 
		self.left = None
		self.right = None
		self.data = data 

	def insert(self, data):
	# Compare the new value with the parent node
		if self.data:
		    if data < self.data:
		        if self.left is None:
		            self.left = Node(data)
		        else:
		            self.left.insert(data)
		    elif data > self.data:
		        if self.right is None:
		            self.right = Node(data)
		        else:
		            self.right.insert(data)
		else:
		    self.data = data

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











red black tree insert
