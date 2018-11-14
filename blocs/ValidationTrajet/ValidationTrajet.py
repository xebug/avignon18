# encoding: utf-8
import requests

# Groupe 5 (TETAH Nesrine, PORQUEZ William, RASSU Michael, SERVILLAT Fabien)

id_client=OxF40831 #example
id_chauffeur=0x97324 #example
id_course=0xC2497 #example

choixFait = False
choixLitige = False

def TrajetAccepte(): # On suppose que le trajet a été accepté précédemment
    global dateTrajetAccepte='14/11/2018:14:01' # Date qui aurais ete renvoyé par le trajet effectué
    global dateMaximalPlainte='15/11/2018:14:01' # Date calculé automatiquement 1j apres
    global prixTrajet = '5.58'
    return true; # On suppose que le trajet a été accepté précédemment


def payementChauffeur(prixTrajet,id_chauffeur): # prix trajet envoyé au chauffeur cible
    r = requests.get('http://localhost:5000/payment/price='+prixTrajet+'&driver='+id_chauffeur)

def mettreNote(id_utilisateur): # Fonction pour noter sur 5 un utilisateur (chauffeur ou client)
    note = raw_input("Choisissez votre note de 1 à 5")
    if note not in ['1', '2', '3', '4', '5']:
        print "Choix incorrect !"
    else:
        r = requests.get('http://localhost:5000/note/noteChoisi='+note+'&userRated='+id_chauffeur)


def CreationLitige(id_client,id_chauffeur,id_course):
    while choixLitige==False
        print "Choisissez votre type de litige : "
        i = raw_input("1:Chauffeur non venu au lieu de RDV, 2:Le chauffeur ne m'a pas déposé au bon endroit, 3:Autres type litige")
        if i not in ['1', '2', '3']:
            print "Choix incorrect !"
        else:
            if i=='1'
                typeLitige = "Chauffeur non venu au lieud de RDV"
                r = requests.get('http://localhost:5000/litige/typeLitige='+typeLitige+'&users='+id_client'&driver='+id_chauffeur)
            if i=='2'
                typeLitige = "Chauffeur ne m'a pas deposé au bon endroit"
                gpsGetMyPosition="POSITIONGPSHACH" # position GPS haché
                r = requests.get('http://localhost:5000/litige/typeLitige='+typeLitige+'&users='+id_client'&driver='+id_chauffeur+'&gps='+gpsGetMyPosition)
                #Dans le cas ou le chauffeur n'a pas déposé le client au bon endroit la coordonnée gps est fourni avec
            if i=='3'
                typeLitige = raw_input("Decrivez votre litige")
                gpsGetMyPosition="POSITIONGPSHACH" # position GPS haché
                r = requests.get('http://localhost:5000/litige/typeLitige='+typeLitige+'&users='+id_client'&driver='+id_chauffeur+'&gps='+gpsGetMyPosition)

def CreationLitigeChauffeur(id_client,id_chauffeur,id_course):
    while choixLitige==False
        print "Choisissez votre type de litige : "
        i = raw_input("1:Client n'est pas au point de RDV, 2:Autres type litige")
        if i not in ['1', '2']:
            print "Choix incorrect !"
        else:
            if i=='1'
                typeLitige = "Chauffeur non venu au lieud de RDV"
                r = requests.get('http://localhost:5000/litige/typeLitige='+typeLitige+'&users='+id_client'&driver='+id_chauffeur)
            if i=='2'
                typeLitige = raw_input("Decrivez votre litige")
                gpsGetMyPosition="POSITIONGPSHACH" # position GPS haché
                r = requests.get('http://localhost:5000/litige/typeLitige='+typeLitige+'&users='+id_client'&driver='+id_chauffeur+'&gps='+gpsGetMyPosition)
                #On fourni la position gps qui peut servir dans un autres type de litige


def ValidationTrajet():
    mettreNote(id_chauffeur)
    payementChauffeur(prixTrajet,id_chauffeur)




if(TrajetAccepte():
    while(dateTrajetAccepte<dateMaximalPlainte) #tant qu'il est dans les 24h apres le Trajet
        while choixFait==False
            i = raw_input("Choisissez 1 pour valider votre trajet ou 2 pour creer un litige: ")
            if i not in ['1', '2']:
                print "Choix incorrect !"
            else:
                if i=='1'
                    ValidationTrajet()
                if i=='2'
                    CreationLitige(id_client,id_chauffeur,id_course)
    ValidationTrajet() # au bout de 24h
