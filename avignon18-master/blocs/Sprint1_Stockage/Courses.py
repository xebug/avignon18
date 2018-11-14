from datetime import *
from random import *

course = {}

def user(id_u,nom,prenom,position):
	user = {}
	user["id"] = id_u
	user["nom"] = nom
	user["prenom"] = prenom
	user["position"] = position
	return user

def conducteur(id_c,nom,prenom,position):
	conducteur = {}
	conducteur["id"] = id_c
	conducteur["nom"] = nom
	conducteur["prenom"] = prenom
	conducteur["position"] = position
	return conducteur

def ajouter_course(conducteur,user,prix,dist,depart,arrive,heure_depart,heure_arrive):
	date = datetime
	date = str(date)
	date.replace(" ","")
	course ={}
	course["id_course"] = random()
	course["id_chauffeure"] = conducteur["id"]
	course["id_user"] = user["id"]
	course["prix"] = prix
	course["dist"] = dist
	course["depart"] = depart
	course["arrive"] = arrive
	course["heure_depart"] = heure_depart
	course["heure_arrive"] = heure_arrive
	course["date_transaction"] = date
	return course

def creation_fichier(course):
	date = datetime.now()
	date = str(date)
	date.replace(" ","")
	fichier = open("data_"+str(date)+".txt", "w")
	course = str(course)
	fichier.write(course)
	fichier.close()

user_1 = user("156","Bouzid","Fares","Alger") 

conducteur_1 = conducteur("154","Cadi","Hamza","Agadir_la_base")

course_1 = ajouter_course(user_1,conducteur_1,"15000","50","Alger","Agadir","17:50:30","19:32:15")

creation_fichier(course_1)


