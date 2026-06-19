
***

# Datasheet du dataset – Modèle de scoring crédit

***

# 1. Contexte du traitement

## 1.1 Finalité

> Évaluation automatisée du risque de défaut dans le cadre de l’octroi de crédit à des clients particuliers.

## 1.2 Type de traitement

* Décision individuelle automatisée (scoring)
* Traitement de données personnelles

## 1.3 Base légale

* Exécution d’un contrat
* Intérêt légitime (gestion du risque d'octroit de crédit)

## 1.4 Provenance des données

| Source               | Description                                | Risques associés               |
| -------------------- | ------------------------------------------ | ------------------------------ |
| Données déclaratives | Informations fournies par le client        | Biais déclaratif               |
| Historique bancaire  | Données internes (crédits, remboursements) | Biais historique               |


## 1.5 Personnes concernées

* Clients ou prospects (personnes physiques)

***

# 2. Description et caractérisation des variables

## 2.1 Typologie générale

| Type                    | Exemples                           |
| ----------------------- | ---------------------------------- |
| Numériques              | montant\_credit, age, taux\_effort |
| Catégorielles nominales | emploi, logement                   |
| Catégorielles ordinales | historique\_credit                 |

***

## 2.2 Détail des variables

Le tableau ci-dessous liste les variables et indique la décision de conserver ou non chaque variable.

la motiviation est donnée par la colonne Risque proxy :
- Faible - proxy probable : variable très susceptible de reconstruire une caractéristique protégée (ex. code_postal pour origine / niveau socio-économique, anciennete_emploi pour âge) ;
- Moyen/Elevé - proxy possible : variable pouvant devenir problématique par combinaison avec d’autres ;

Nous soulignons également les variables métier légitimes mais sensibles à surveiller (ex. epargne, emploi) ;



| Variable              | Type         | Nature RGPD            | Rôle ML | Risque proxy (biais) | Décision                 |
| --------------------- | ------------ | ---------------------- | ------- | -------------------- | ------------------------ |
| numero\_client        | nominale     | identifiant indirect   | aucun   | *pas d'intérêt*      | ❌ supprimée             |
| nom                   | nominale     | identifiant direct     | aucun   | *pas d'intérêt*      | ❌ supprimée             |
| prenom                | nominale     | identifiant direct     | aucun   | pas d'intérêt        | ❌ supprimée             |
| sexe                  | nominale     | identifiant indirect   |         | très élevé           | ❌ supprimée             |
| date de naissance     | nominale     | identifiant indirect   |         | élevé                | ❌ supprimée             |
| email                 | nominale     | identifiant direct     | aucun   | élevé                | ❌ supprimée             |
| telephone\_mobile     | nominale     | identifiant direct     | aucun   | élevé                | ❌ supprimée             |
| adresse               | nominale     | identifiant direct     | aucun   | élevé                | ❌ supprimée             |
| code\_postal          | nominale     | identifiant indirect   | feature | élevé (socio-éco)    | ❌ supprimée             |
| ville                 | nominale     | identifiant indirect   | feature | élevé (socio-éco)    | ❌ supprimée             |
| IBAN                  | nominale     | identifiant direct     | aucun   | pas d'intérêt        | ❌ supprimée             |
| num\_secu             | nominale     | identifiant fort (NIR) | aucun   | très élevé           | ❌ supprimée             |
| statut_compte_courant | ordinale     | métier                 | feature | pas d'intérêt        | ✅ conservée             |
| duree_credit_mois     | numerique    | métier                 | feature |                      | ✅ conservée             |
| historique\_credit    | ordinale     | métier                 | feature | faible               | ✅ conservée             |
| objet_credit          | nominale     | métier                 |         | *pas d'intérêt*      | ❌ supprimée             |
| montant\_credit       | numérique    | métier                 | feature | faible               | ✅ conservée             |
| epargne               | numérique    | métier                 | feature | éco                  | ⚠️ surveillée            |
| anciennete\_emploi    | numérique    | indirecte              | feature | élevé (socio-éco)    | ⚠️ surveillée            |
| taux\_effort          | numérique    | métier                 | feature | faible               | ✅ conservée             |
| statut_personnel_sexe | nominale     | identifiant indirect   |         | très élevé           | ❌ supprimée             |
| autres_debiteurs      | nominale     | métier                 | feature |                      | ✅ conservée             |
| anciennete_logement   | numerique    | métier                 | feature | proxy socio-éco      | ⚠️ surveillée            |
| biens                 | nominale     | métier                 | feature | proxy socio-éco      | ⚠️ surveillée            |
| age                   | numérique    | indirecte              | feature | proxy âge            | ⚠️ surveillée            |
| autres_credits        | nominale     | métier                 | feature |                      | ✅ conservée             |
| logement              | catégorielle | indirecte              | feature | proxy richesse       | ⚠️ surveillée            |
| nb_credits_existants  | numerique    | métier                 | feature |                      | ✅ conservée             |
| emploi                | catégorielle | indirecte              | feature | proxy socio-éco      | ⚠️ surveillée            |
| nb_personnes_charge   | numerique    | métier                 | feature | proxy socio-éco      | ⚠️ conservée             |
| telephone_declare     | nominale     |                        |         | *pas d'intérêt*      | ❌ supprimée             |
| travailleur_etranger  | nominale     | identifiant indirect   | aucun   | proxy socio-éco      | ❌ supprimée             |
| defaut                | binaire      | cible                  | target  | -                    | ✅ entraînement          |



***

# 3. Données personnelles et niveau de risque

## 3.1 Classification

### Données à identification directe

Les données à identification directe sont des données sensibles et sont supprimées :
- nom, prénom, num_secu, email, etc...

***

### Données indirectement identifiantes

Les données à identification indirecte peuvent être conservées, en respectant le principe de minimisation. Ces données doivent être surveillées.

***

### Données à risque de discrimination

| Variable               | Risque potentiel                     |
| ---------------------- | ------------------------------------ |
| emploi                 | catégorie socio-professionnelle      |
| logement               | niveau socio-économique              |
| epargne                | richesse                             |
| anciennete\_emploi     | proxy âge / niveau socio-économique  |
| ville\_code postal     | proxy géo / niveau socio-économique  |
| sexe\_Statut personnel | catégorie sociale                    |
| travailleur_etranger   | catégorie sociale                    |


***

# 4. Analyse des biais

## 4.1 Biais identifiés

### Biais historiques

* Les données reflètent des décisions passées
* Risque de reproduction des discriminations

### Biais de sélection

* Population non représentative

### Biais de proxy

* Variables neutres corrélées à des caractéristiques protégées

***

## 4.2 Analyse des proxies

> Certaines variables apparemment neutres présentent des corrélations fortes avec des caractéristiques protégées et peuvent induire une discrimination indirecte.

Exemple :

* code\_postal → proxy de richesse / origine
* emploi → proxy de classe sociale

***

# 5. Mesures de mitigation

## 5.1 Minimisation des données

* suppression des identifiants directs
* suppression des variables non pertinentes

***

## 5.2 Transformation

| Variable        | Transformation         |
| --------------- | ---------------------- |
| code\_postal    | regroupement en région |




## 5.4 Mesures organisationnelles

* supervision humaine possible
* documentation du modèle
* explicabilité des décisions

***

# 6. Risques résiduels

## 6.1 Risques persistants

| Risque                 | Description                        |
| ---------------------- | ---------------------------------- |
| Proxy combiné          | combinaison de variables           |
| Biais socio-économique | lié à la finalité crédit           |
| Biais historique       | reproduction des pratiques passées |
| Boîte noire            | interactions complexes             |

***

## 6.2 Justification

> Certaines variables à risque sont conservées car nécessaires à la finalité de scoring. Leur suppression dégraderait significativement la capacité prédictive du modèle.

***

## 6.3 Acceptation du risque

* validation métier
* validation conformité
* documentation des arbitrages

***

# 7. Conclusion

> Le dataset a fait l’objet d’une analyse approfondie au regard des exigences RGPD (minimisation, proportionnalité) et des risques de discrimination indirecte.  
> Malgré les mesures prises, des risques résiduels subsistent liés aux variables proxy et aux biais structurels des données.


