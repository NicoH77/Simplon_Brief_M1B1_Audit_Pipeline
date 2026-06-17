# M2 B2 - Analyse éthique et conformité du jeu de données
---

## Étape 1 : Caractériser les variables

- Variable numérique : Représente une quantité mesurable
- Variable catégorielle nominale : Représente des catégories sans ordre ni hiérarchie. Les valeurs sont des étiquettes.
- Variable catégorielle ordinale : Représente des catégories avec un ordre ou une hiérarchie, mais sans distance numérique précise entre les niveaux.
- 


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
- statut_compte_courant
- duree_credit_mois
- historique_credit
- objet_credit
- montant_credit
- epargne
- anciennete_emploi
- taux_effort
- statut_personnel_sexe     : identification par recoupement (indirecte) => variable discriminatoire à exclure (pour raison d'équité)
- autres_debiteurs
- anciennete_logement
- biens
- age                      : identification par recoupement (indirecte)
- autres_credits
- logement
- nb_credits_existants
- emploi
- nb_personnes_charge      : => variable pouvant introduire un biais socio-économique
- telephone_declare
- travailleur_etranger     : identification par recoupement (indirecte) => variable discriminatoire à exclure (pour raison d'équité)
- defaut


