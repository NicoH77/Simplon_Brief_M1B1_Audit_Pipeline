# M2 B2 - Analyse éthique et conformité du jeu de données
---

## Étape 1 : Caractériser les variables

- Variable numérique : Représente une quantité mesurable
- Variable catégorielle nominale : Représente des catégories sans ordre ni hiérarchie. Les valeurs sont des étiquettes.
- Variable catégorielle ordinale : Représente des catégories avec un ordre ou une hiérarchie, mais sans distance numérique précise entre les niveaux.


Liste des variables du jeu de données complet :

- numero_client     : Catégorielle nominale
- nom               : Catégorielle nominale - décrit une personne
- prenom            : Catégorielle nominale - décrit une personne 
- sexe              : Catégorielle nominale - décrit une personne 
- date_naissance    : Catégorielle nominale - décrit une personne 
- email             : Catégorielle nominale - décrit une personne
- telephone_mobile  : Catégorielle nominale - décrit une personne 
- adresse           : Catégorielle nominale - décrit une personne
- code_postal       : Catégorielle nominale
- ville             : Catégorielle nominale
- iban              : Catégorielle nominale - décrit une personne
- num_secu          : Catégorielle nominale - décrit une personne
- statut_compte_courant : Catégorielle ordinale
- duree_credit_mois     : Numérique
- historique_credit     : Catégorielle nominale
- objet_credit          : Catégorielle nominale 
- montant_credit        : Numérique
- epargne               : Catégorielle ordinale
- anciennete_emploi     : Catégorielle ordinale - décrit une personne
- taux_effort           : Numérique
- statut_personnel_sexe : Catégorielle nominale - décrit une personne 
- autres_debiteurs      : Catégorielle nominale 
- anciennete_logement   : Numérique  - décrit une personne
- biens                 : Catégorielle nominale 
- age                   : Numerique
- autres_credits        : Catégorielle nominale 
- logement              : Catégorielle nominale 
- nb_credits_existants  : Numerique
- emploi                : Catégorielle nominale - décrit une personne 
- nb_personnes_charge   : Numerique
- telephone_declare     : Catégorielle nominale 
- travailleur_etranger  : Catégorielle nominale - décrit une personne 
- defaut                : Catégorielle nominale 


## Étape 2 : Analyse réglementaire (RGPD)

Les variables métiers sont de variables légitimes pour un model de crédit, car elles ont un lien avec la solvabilité.


- numero_client             : identification par recoupement (indirecte) => à exclure car identifiant interne sans pouvoir prédictif (on suppose que l'ID ne préjuge pas de l'ancienneté du client)
- nom                       : identification directe => à exclure du jeu de données
- prenom                    : identification directe => à exclure
- sexe                      : identification par recoupement (indirecte) => variable discriminatoire à exclure (pour raison d'équité)
- date_naissance            : identification par recoupement (indirecte)
- email                     : identification directe => à exclure
- telephone_mobile          : identification directe => à exclure
- adresse                   : identification directe => à exclure
- code_postal               : identification par recoupement (indirecte) => variable pouvant introduire un biais socio-économique
- ville                     : identification par recoupement (indirecte) => variable pouvant introduire un biais socio-économique
- iban                      : identification directe => à exclure
- num_secu                  : identification directe => à exclure
- statut_compte_courant     : variable métier
- duree_credit_mois         : variable métier
- historique_credit         : variable métier
- objet_credit              : variable métier
- montant_credit            : variable métier
- epargne                   : variable métier
- anciennete_emploi         : variable métier
- taux_effort               : variable métier
- statut_personnel_sexe     : identification par recoupement (indirecte) => variable discriminatoire à exclure (pour raison d'équité)
- autres_debiteurs          : variable métier
- anciennete_logement       : variable métier
- biens                     : variable métier
- age                       : identification par recoupement (indirecte)
- autres_credits            : variable métier
- logement                  : variable métier
- nb_credits_existants     : variable métier
- emploi                    : variable métier
- nb_personnes_charge      : => variable pouvant introduire un biais socio-économique
- telephone_declare
- travailleur_etranger     : identification par recoupement (indirecte) => variable discriminatoire à exclure (pour raison d'équité)
- defaut

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


Malgré la suppression des variables sensibles, le modèle reste exposé à des biais indirects via des variables proxy (géographiques, socio-économiques ou professionnelles). La conformité RGPD ne garantit donc pas l’équité du modèle.

## Étape 4 : Produire le datasheet



