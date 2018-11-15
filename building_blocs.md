# Groupes jeudi:

/!\ Tous les groupes doivent feront du code, vous avez 6h.

1. Calculer un score robuste **ET** équitable
          ALCARAZ
          AMOUZOUN
          NDIAYE
          SERVILLAT
     ```python
    
     # Base de donnée contenant l'historique des sequences de demandes de
     # mise à jour de rank.
     # { id: [(src, rank), ...], ...}
     # Example: {1:[(10,4), (10,4), (42, 1), (69, 1), (96, 1), (10,4), (10,4), (10,4), (10,4)]}
     # où le noeud d'ID = 1 a reçu d'abord 4* de 10, puis de nouveau 4 de 10, puis 1 de 42, etc.
     db = dict()
 
     def compute_rank(src, dst, rank, db):
     """
     src: identifiant de celui qui veut donner le rank
     dst: identifiant de celui qui voit sont rank mis à jour
     rank: proposition de rank

     return valeur du rank sur base de la nouvelle proposition et de l'historique.
     """
    ```

2. Generare un identifiant qui comprend une partie immuable 

    ```python
    def getCurrentLocation(anonymized=False):
    """
    anonymized: si on veut ou non la localisation exacte.
    return la localisation actuelle du noeud
    """

    def genMyId():
    """
    return un identifiant unique pour le noeud
    """

    def genNetworkId():
    """
    return un identifiant unique pour le noeud qui prend en compte la localisation
    """
    ```

3. Implémenter une API pour serveur de découverte de noeuds (et un simulateur de client)
    En Flask:
    
    ```
    GET /nodes/         liste de tous les IDs des noeuds connus
    GET /node/<ID>      information sur le noeud ID
    POST /node/<ID>     ajouter ou mettre à jour le noeud ID
    ```
    
    Les données sont toutes envoyées en JSON. A vous de définir les information que vous mettez (pensez à la vie privée mais aussi à l'autenticité des donnée.

4. Calculer un block
    ```python
    
    class Block:
    """Representation d'un block"""
    ...
    
    
    # La blockchaine est simulé par une simple liste où l'entré i correspond au i'eme  block. On ne
    # supporte pas les forks.
    # Exemple: blockchain = [b1, b2, b3] signifie que le premier block est b1, suivi de b2, puis de b3.
    blockchain = list()
    
    def computeBlock(transactions):
    """
    transactions: la liste des transactions à mettre dans la block
    return le bloc avec son contenu et sa preuve.
    """
    
    def hashBlock(block):
    """
    block: block pour lequel calculer le hash
    return: le hash du block
    """
    
    def electBlock(blocs):
    """
    blocs: liste des blocs parmis lesquel en choisir un
    return le bloc qui a gagné
    """
    #Exemple d'utilisation: 
    b1 = computeBlock(["t1", "t3", "t2"])
    b2 = computeBlock(["t1", "t2"])
    new_block = electBlock([b1,b2])
    blockchain.append(new_block)
    ```
5. Stockage de données protégées avec schéma de shamir

    ```python
    
    def generatePolynome(secret, k)
    """
    secret: le secret à protéger (un entier)
    k: la degré du polynome à générer
    
    return les parametres du polynome de degré k à utiliser sous forme de liste.
           Par exemple si retourne [secret, 4, 19] il s'agit du polynome y = secret + 4 * x + 19 * x^2
    """
    
    def computeX(polynome, x):
    """
    polynome: parametres du polynome
    x: valeur en x lequel calculer y
    
    return y = f(x) pour f le polynome défini par `polynmome`
    """
    
    def storeSecret(secret, k, id):
    """
    secret: secret à stocker
    k: nombre minimum de noeuds qui doivent se mettre en commun pour reconstruire `secret`
    id: identifiant du noeud où stocker le secret
    
    return: la valeur transformée du secret comme elle devrait être stockée par le noeud `id`
    """
    ```


# Travaux mardi et mercredi:

* Blockchain

  * Identifiants - Groupe 1 (DESTREE Gabriel, RASSU Michael, BENCHRIFA Mohamed Amine, AMINE KHODJA Ahmed Ramy)
  * Demande de trajet
  * Acceptation d’un trajet : ADDA Ahlem Lamia, PORQUEZ William , SANNI Habil , BM


  * Validation d’un trajet effectué - Groupe 5 (TETAH Nesrine, PORQUEZ William, RASSU Michael, SERVILLAT Fabien),  ADDA Ahlem, ALCARAZ Hugo, ISLAHI Chaimae, NDIAYE Samba Oumar
  * Mining : ALCARAZ BAUMEL EL KADOURI SERVILLAT
  * Choix de la branche
  
* Réseau:
  * Découverte de noeuds
  * Routage des messages entre les noeuds (DESTREE Gabriel, BENCHRIFA Mohamed, BOUZID Fares, AMAZOUNE Marc, KANE Ababakar)
  * Broadcast de messages
  
* Stockage
  * Stockage des données 
  * Récupération des données en cas de litige

* Confiance
  * Calcul robuste du ranking
  * Identification des conducteurs/clients


