# M2 B2 - Analyse éthique et conformité du jeu de données
---

## Étape 1 : Caractériser les variables

- Variable numérique : Représente une quantité mesurable
- Variable catégorielle nominale : Représente des catégories sans ordre ni hiérarchie. Les valeurs sont des étiquettes.
- Variable catégorielle ordinale : Représente des catégories avec un ordre ou une hiérarchie, mais sans distance numérique précise entre les niveaux.


Liste des variables du jeu de données complet :

| Variable              	| Type    		        | Caractéristique= RGPD  | 
| ------------------------- | --------------------- | ---------------------- |
| numero_client     		| Catégorielle nominale | 						 | 
| nom               		| Catégorielle nominale | décrit une personne    |
| prenom            		| Catégorielle nominale | décrit une personne    |
| sexe              		| Catégorielle nominale | décrit une personne    |
| date_naissance    		| Catégorielle nominale | décrit une personne    |
| email             		| Catégorielle nominale | décrit une personne    |
| telephone_mobile  		| Catégorielle nominale | décrit une personne    |
| adresse           		| Catégorielle nominale | décrit une personne    |
| code_postal       		| Catégorielle nominale	|                        |
| ville             		| Catégorielle nominale	|                        |
| iban              		| Catégorielle nominale | décrit une personne    |
| num_secu          		| Catégorielle nominale | décrit une personne    |
| statut_compte_courant 	| Catégorielle ordinale	|                        |
| duree_credit_mois     	| Numérique				|                        |
| historique_:credit     	| Catégorielle nominale	|                        |
| objet_credit          	| Catégorielle nominale |                        |
| montant_credit        	| Numérique				|                        |
| epargne                	| Catégorielle ordinale	|                        |
| anciennete_emploi     	| Catégorielle ordinale | décrit une personne    |
| taux_effort           	| Numérique				|                        |
| statut_pers:onnel_sexe 	| Catégorielle nominale | décrit une personne    |
| autres_debiteurs      	| Catégorielle nominale |                        |
| anciennete_logement   	| Numérique				| décrit une personne    |
| biens                 	| Catégorielle nominale |                        |
| age                   	| Numerique				|                        |
| autres_credits        	| Catégorielle nominale |                        |
| logement              	| Catégorielle nominale |                        |
| nb_credits_existants  	| Numerique				|                        |
| emploi                	| Catégorielle nominale | décrit une personne    |
| nb_personnes_charge   	| Numerique				|                        |
| telephone_d:eclare     	| Catégorielle nominale |                        |
| travailleur _etranger  	| Catégorielle nominale | décrit une personne    |
| defaut                	| Catégorielle nominale |                        |


## Étape 2 : Analyse réglementaire (RGPD)

Les variables métiers sont de variables légitimes pour un model de crédit, car elles ont un lien avec la solvabilité.



| Variable              	| Caractéristique RGPD  		             | Analyse reglementaire                                                    | 
| ------------------------- | ------------------------------------------ | ------------------------------------------------------------------------ |
| numero_client             | identification par recoupement (indirecte) | à exclure car identifiant interne sans pouvoir prédictif					| 
| nom                       | identification directe 					 | à exclure - donnée sensible et individuelle                              |
| prenom                    | identification directe 					 | à exclure - donnée sensible et individuelle                              |
| sexe                      | identification par recoupement (indirecte) | à exclure - variable discriminatoire                                     |
| date_naissance            | identification par recoupement (indirecte) | à minimiser - prendre l'age                                              |
| email                     | identification directe 					 | à exclure - donnée sensible et individuelle                              |
| telephone_mobile          | identification directe 					 | à exclure - donnée sensible et individuelle                              |
| adresse                   | identification directe 					 | à exclure - donnée sensible et individuelle                              |
| code_postal               | identification par recoupement (indirecte) | à exclure - variable pouvant introduire un biais socio-économique        |
| ville                     | identification par recoupement (indirecte) | à exclure - variable pouvant introduire un biais socio-économique        |
| iban                      | identification directe 					 | à exclure - donnée sensible et individuelle                              |
| num_secu                  | identification directe 					 | à exclure - donnée sensible et individuelle                              |
| statut_compte_courant     | variable métier                            | OK conformité, vérifier équité                                           |
| duree_credit_mois         | variable métier                            | OK conformité, vérifier équité                                           |
| historique_credit         | variable métier                            | OK conformité, vérifier équité                                           |
| objet_credit              | variable métier                            | OK conformité, vérifier équité                                           |
| montant_credit            | variable métier                            | OK conformité, vérifier équité                                           |
| epargne                   | variable métier                            | OK conformité, vérifier équité                                           |
| anciennete_emploi         | variable métier                            | OK conformité, vérifier équité                                           |
| taux_effort               | variable métier                            | OK conformité, vérifier équité                                           |
| statut_personnel_sexe     | identification par recoupement (indirecte) | à exclure - variable discriminatoire                                     |
| autres_debiteurs          | variable métier                            | OK conformité, vérifier équité                                           |
| anciennete_logement       | variable métier                            | OK conformité, vérifier équité                                           |
| biens                     | variable métier                            | OK conformité, vérifier équité                                           |
| age                       | identification par recoupement (indirecte) | OK conformité, vérifier équité                                           |
| autres_credits            | variable métier                            | OK conformité, vérifier équité                                           |
| logement                  | variable métier                            | OK conformité, vérifier équité                                           |
| nb_credits_existants      | variable métier                            | OK conformité, vérifier équité                                           |
| emploi                    | variable métier                            | OK conformité, vérifier équité                                           |
| nb_personnes_charge       | identification par recoupement (indirecte) | variable pouvant introduire un biais socio-économique                    |
| telephone_declare         |                                            | à exclure - n'apporte                                                    |
| travailleur_etranger      | identification par recoupement (indirecte) | à exclure - variable discriminatoire                                     |
| defaut                    | -  									     |	-																		|


## Étape 3 : Analyse des biais

Certaines variables peuvent remplacer implicitement une variable sensible supprimée. On appelle ces variables "variables proxy"

Proxy du sexe / genre 
même en excluant la variable `sexe`, certaines varaible peuvent s'en rapprocher
- statut_personnel_sexe : contient explicitement le sexe
- nb_personnes_charge : distribution différente H/F
- anciennete_emploi : interruptions de carrière potentielles

Proxy de l’origine / nationalité
- travailleur_etranger : quasi direct
- ville / code_postal : corrélé à origine socio-éco ou migratoire
- logementtypologie territoriale (quartier)
- anciennete_logement : stabilité géographique liée à origine


Une variable proxy constitue une sorte de "raccourci" statistique pour contourner l’absence de données directes, mais son utilisation nécessite une validation rigoureuse de sa pertinence et de ses limites. Ces variables peuvent être sujettes à des biais. L'identification du biais repose sur l’analyse de sa relation avec d'autres varaibles et les risques de distorsion qu’elles introduisent.

> Malgré la suppression des variables sensibles (reglementation RGPD), le modèle reste exposé à des biais indirects via des variables proxy (géographiques, socio-économiques ou professionnelles). La conformité RGPD ne garantit donc pas l’équité du modèle.


## Étape 4 : Produire le datasheet

[Datasheet]: https://github.com/NicoH77/Simplon_Brief_M1B1_Audit_Pipeline/blob/8bb2f4cfe3ad4cad8ade5d92cc46dcf2514f8502/M2B2_Datasheet.md

Voir le document [M2B2_Datasheet] [Datasheet]

## Étape 5 : Du jeu « techniquement propre » au jeu « éthiquement exploitable »

L'objectif de cette étape est  de passer du jeu de données techniquement nettoyé à un jeu de données exploitable d’un point de vue éthique et réglementaire. Elle repose sur :
- la suppression des identifiants directs et des variables sensibles (conformité RGPD),
- la généralisation des quasi-identifiants afin de limiter les risques de ré-identification,
- la conservation encadrée des variables métier nécessaires à la finalité de scoring,
- l’identification et la documentation des risques résiduels liés aux variables proxy.


Pour finaliser le jeu de données exploitable et éthique, on peut appliquer le principe de proportionalité : chaque variable est évaluée selon son utilité métier vs. son risque éthique.

| Métier        | Ethique           | Décision              |
| ------------- | ----------------- | --------------------- |
| inutile       | risqué ou pas     | Suppression           |
| utile         | faiblement risqué | Conservation          |
| utile         | risqué            | Transformation        |
| indispensable | -                 | Conservation encadrée |


| Variable              | Opération         | Justification                                                |
| --------------------- | ----------------- | ------------------------------------------------------------ |
| numero\_client        | ❌ supprimée      | RGPD                                                         |
| nom                   | ❌ supprimée      | RGPD                                                         |
| prenom                | ❌ supprimée      | RGPD                                                         |
| sexe                  | ❌ supprimée      | Discrimination 	                                          |
| date de naissance     | ❌ supprimée      | Minimisation (on prend l'age voire une tranche)              |
| email                 | ❌ supprimée      | RGPD                                                         |
| telephone\_mobile     | ❌ supprimée      | RGPD                                                         |
| adresse               | ❌ supprimée      | RGPD                                                         |
| code\_postal          | ⚠️ supprimée      | potentiel Biais - possibilité de généraliser                 |
| ville                 | ⚠️ supprimée      | potentiel Biais - possibilité de généraliser                 |
| IBAN                  | ❌ supprimée      | RGPD                                                         |
| num\_secu             | ❌ supprimée      | RGPD                                                         |
| statut_compte_courant | ✅ conservée      | Variable métier - faible risque de biais                     |
| duree_credit_mois     | ✅ conservée      | Variable métier - faible risque de biais                     |
| historique\_credit    | ✅ conservée      | Variable métier - faible risque de biais                     |
| objet_credit          | ✅ supprimée      | Variable métier - faible risque de biais                     |
| montant\_credit       | ✅ conservée      | Variable métier - faible risque de biais                     |
| epargne               | ⚠️ surveillée     | Variable métier - risque de biais                            |
| anciennete\_emploi    | ⚠️ surveillée     | Variable métier - risque de biais                            |
| taux\_effort          | ✅ conservée      | varaible métier - faible risque de biais                     |
| statut_personnel_sexe | ❌ supprimée      | Discrimination   |                                           |
| autres_debiteurs      | ✅ conservée      | Variable métier - faible risque de biais                     |
| anciennete_logement   | ⚠️ surveillée     | Variable métier - risque de biais                            |
| biens                 | ⚠️ surveillée     | Variable métier - risque de biais                            |
| age                   | ⚠️ surveillée     | Variable métier - risque de biais possibilité de généraliser |
| autres_credits        | ✅ conservée      | Variable métier - faible risque de biais                     |
| logement              | ⚠️ surveillée     | Variable métier - risque de biais                            |
| nb_credits_existants  | ✅ conservée      | Variable métier - faible risque de biais                     |
| emploi                | ⚠️ surveillée     | Variable métier - risque de biais                            |
| nb_personnes_charge   | ⚠️ conservée      | Variable métier - risque de biais                            |
| telephone_declare     | ❌ supprimée      | Inutile                                                      |
| travailleur_etranger  | ❌ supprimée      | Discrimination                                               |
| defaut                | ✅ entraînement   | cible                                                        |


Risque résiduel :
Malgré la suppression des identifiants directs et des variables explicitement sensibles, un risque résiduel de discrimination indirecte subsiste. En effet, certaines variables conservées, bien que nécessaires à la finalité de scoring crédit, sont susceptibles d’agir comme variables proxy de caractéristiques protégées.
- Les variables code_postal (généralisé en région) et ville peuvent ainsi refléter des disparités territoriales corrélées à l’origine ou au niveau socio-économique.
- Les variables emploi, logement, epargne et biens constituent des indicateurs pertinents de solvabilité, mais restent fortement corrélés à la situation socio-économique, pouvant ainsi introduire des biais indirects. Ces variables sont conservées car elles sont nécesaires à la finalité du modèle et impossible à remplacer.

Par ailleurs, le risque peut être amplifié par la combinaison de plusieurs variables, notamment géographiques et socio-professionnelles (par exemple : région + emploi + logement). Enfin, le modèle étant entraîné sur des données historiques, il existe un risque de reproduction de biais préexistants dans les décisions passées.




## Étape 5 : Étape 6 (Optionnelle) : Quantifier plutôt qu'affirmer

Les risques résiduels sont lié aux variables contribuant directement à l’évaluation du risque de crédit. Ils doivent toutefois faire l’objet de mesures de limitation et doivent être explicitement documentés et surveillés dans le temps, notamment via des audits réguliers d’équité et de performance du modèle. Jusqu'à présent, les recommandations reponsent sur notre jugement, mais il existe des techniques pour étayer et quantifier certains niais et déséquilibres.




