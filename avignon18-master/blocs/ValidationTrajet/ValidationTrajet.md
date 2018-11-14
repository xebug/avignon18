TETAH Nesrine										M1 SICOM
PORQUEZ William
RASSU Michael 
SERVILLAT Fabien





Validation de trajet effectué



On prend en compte que le paiement procède de la manière suivante :    
Paiement :
Phase d’acceptation du trajet :
- le client possède un certain nombre de crédit 
    	- le chauffeur modifie son tarif selon le trajet
    	- Si acceptation : 
        		- client transfère les crédits au chauffeur
    	- Sinon :
        		- Le chauffeur peut changer son tarif
        	- si ok: 
            		- client réserve le trajet
        	- sinon : 
            		- client réserve un autre trajet 
                
                
Notre étape de paiement : 

Le paiement est effectué lorsque le client est déposé. Mais la transaction débute lorsque le trajet est accepté. Et il se termine soit dans le cas où les deux parties confirme 

Notre étape de validation :

Dans un premier temps, certaines conditions doivent être vérifié pour que l'étape de "Validation du trajet" soit acceptée. La première condition à avoir est que les deux parties donc client et chauffeur doivent être connecté à l'application. Authentifié et vérifié, si ces deux conditions ne sont pas validées alors aucun des deux ne pourra pas alors valider son trajet ou valider le dépôt du passager. Lorsque ces conditions seront vérifiées, le client doit transmettre sa position avec un hash et un nonce généré et doit valider sa position de destination pour qu'il soit en conformité avec le point B prévu initialement. Cela permet de transmettre les données géographiques sans renseigner des données personnelles. De plus retrouver la valeur du hash initial est très difficile. Et selon la notation les autres personnes pourront se poser des questions sur la personne qui informe qu'il n'a pas été déposé à l'endroit voulu mais lorsqu'on regarde les données géographiques on s'aperçoit qu'il se retrouve à un endroit non accessible selon le temps estimé. Dans le même cas le chauffeur doit aussi valider sa position lorsqu'il dépose le client.

Le cas de validation de trajet est confirmé à partir du moment que les deux parties sont en accord. C'est à dire, le client confirme bien qu'il est arrivé à destination dans les délais prévu. Le chauffeur confirme de son côté qu'il a déposé le client au point de rendez-vous. Les deux parties confirment soit par le biais de l'application ou alors à l'aide d'un code que le client a reçu lors de l'étape d'acceptation du trajet, puis il le fourni au chauffeur pour que celui confirme de son côté. Si le client met en attente la validation, après une durée de 24h la transaction est effectuée. 

On rentre dans le cas de litige lorsque :

Le client informe et prouve avec ses coordonnées GPS qu'il n'est pas au point de destination. Uber vérifiera avec les coordonnées du chauffeur selon l'heure indiqué du client. Le chauffeur lors du dépôt du client doit confirmer avec une preuve GPS qu’il a bien déposer le client à l'endroit voulu sans quoi la transaction ne sera pas validée. 
Le client effectue bien le trajet avec le chauffeur mais celui-ci n'arrive pas dans les temps estimés. Le chauffeur recevra quand même sa transaction pour donner suite à la confirmation du dépôt du client mais le client aura le droit de déposer un avis insatisfait pour ce conducteur. La mauvaise appréciation donnée par le client sera alors transmise au système d'identifiant du chauffeur qui se chargera du rang de celui-ci ainsi que sa note. 
Le chauffeur informe à Uber que le client n'était pas présent au lieu de rendez-vous et le prouve par donnée GPS. Si le client ne se manifeste pas, le chauffeur sera alors remboursé du trajet qu'il a effectué lorsqu'il a accepté la réservation du client c'est à dire l'emplacement géographique jusqu'au point de rendez-vous. Le prélèvement sera alors débité des crédits du client.
