# -*- coding: utf-8 -*-
"""
pipeline_v1.py — Préparation des données pour le scoring crédit Finova
Auteur : K. Moreau (équipe Data, 2024)

Prépare les dossiers de crédit pour l'entraînement du modèle de scoring :
nettoyage, encodage, normalisation, découpage train/test.

Usage : python pipeline_v1.py [chemin_vers_finova_credits.db]
"""

import sys
import sqlite3

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Chemin vers la base de données Finova Credits
DB_PATH = sys.argv[1] if len(sys.argv) > 1 else "finova_credits.db"

# colonnes inutiles pour le scoring
COLONNES_INUTILES = ["nom", "prenom", "email", "telephone_mobile", "adresse",
                     "ville", "iban", "num_secu", "date_naissance"]


# Fonction de chargement des données depuis la base avec filtrage des colonnes
#      Charge toutes les colonnes de la table dossiers_credit sans filtre.
#      Supprime explicitement certaines colonnes listées dans COLONNES_INUTILES.

def load_data():
    """Charge les dossiers de crédit depuis la base."""
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM dossiers_credit", conn)
    conn.close()
    df = df.drop(columns=COLONNES_INUTILES)
    return df


# Uniformisation des types 
#     - Conversion en numérique, 
#     - Toute valeur invalide (texte, vide, format incorrect) → NaN
#     - Les NaN → remplacés par la moyenne globale de la colonne
# Implication : La fonction remplace toutes les données invalides par une valeur moyenne globale (Les erreurs de saisie sont transformées en moyenne)
#     → Introduction d'une valeur artificielle, potentiellement importante
#     → Introduit un biais non maitrisé

def fix_amounts(df):
    """Corrige la colonne montant_credit et complète les montants manquants."""
    df["montant_credit"] = pd.to_numeric(df["montant_credit"], errors="coerce")
    df["montant_credit"] = df["montant_credit"].fillna(df["montant_credit"].mean())
    return df


# Nettoyage des données 
#     - Supprime toute ligne contenant au moins une valeur NaN (sur n’importe quelle colonne)
# Implication : la fonction ne conserve uniquement que les lignes totalement complètes
#     - le dataset final ne contient pas de valeurs manquantes mais cette fonction peut occasionner une perte importante de données
#     - Le nettoyage n'est pas ciblé : une donnée NaN sur une colonne non critique entraine la suppression de la ligne

def clean_data(df):
    """Supprime les enregistrements invalides."""
    df = df.dropna()
    return df.reset_index(drop=True)


# Encodage des variables
#     - Converti le N° Client en entier => on peut se poser la question de l'interet de cette transformation
#     - Converti le code postal en valeur numérique → si code postal invalide : 0 => idem
#     - Aucune distinction entre variable catégorielle et variable numérique
# Implications :
#     - Pas de validation de l'identifiant client (simple conversion)
#     - valeur artificielle du code postal en cas de d'erreur de saisie
#     - les variables transformées ne représente pas un interet primordial pour le modèle
    
def encode_features(df):
    """Encode les variables catégorielles en numérique."""
    # le numéro client encode l'ancienneté de la relation, on le conserve
    df["numero_client"] = df["numero_client"].str.replace("FIN-", "").astype(int)
    df["code_postal"] = pd.to_numeric(df["code_postal"], errors="coerce").fillna(0).astype(int)

    for col in df.columns:
        if df[col].dtype == object or str(df[col].dtype) == "str":
            df[col] = LabelEncoder().fit_transform(df[col].astype(str))
    return df



# Préparation des datasets
# Séparation X/y
#      - y correspond à la colonne "defaut" :
#      - Normalisation de tout le dataset X
# Implications :
#     - il n'y a eu aucun controle ni aucune transformation sur la colonne "defaut" → quid des valeurs abérantes ?
#     - Le scaler normalise tout le dataset, la séparation entrainement/test ne se faisant qu'après la normalisation
#     - conséquence : Le modèle va indirectement "voir" le test set
#     - L’accuracy affichée sera optimiste et biaisée
#     - Le scalling est appliqué à toutes les colonnes, quelque soit le type de variable (catégorielle et numérique)
#     - transformation de variables discontinues en variables continues : par exemple, le modèle va interpréter une distance numérique entre codes postaux (ce qui n’a pas de sens)
#     - train_test_split : il manque le random_state : le slit sera différent à chaque éxécution et produira des résultats non reproductibles

def prepare_datasets(df):
    """Normalise les données et construit les jeux d'entraînement et de test."""
    X = df.drop(columns=["defaut"])
    y = df["defaut"]

    scaler = StandardScaler()
    X = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    return X_train, X_test, y_train, y_test


# Exécution du pipeline complet
#    SQL brut 
#   → Suppression colonnes (statique)
#   → Conversion montant + remplacement par moyenne
#   → Suppression lignes avec NaN (toutes colonnes)
#   → Transformation ID + code postal
#   → Scaling global (train + test mélangés)
#   → Split aléatoire 80/20

# L'entrainement du modèle entraîne un modèle linéaire standard, sans tuning et sans gestion du déséquilibre de classes
# Implication :  l'Accuracy risque d'être fortement biaisée à cause du data leakage (scaler de tout le dataset), dataset nettoyé brutalement
# Certaines vairables ne sont pas proprement modélisées (Code postal /numéro client)

# Le scaler n'est pas sauvegardé, rendant impossible l'application du même traitement en production

data leakage (scaler)
dataset potentiellement nettoyé agressivement

def main():
    df = load_data()
    print(f"Dossiers chargés : {len(df)}")

    df = fix_amounts(df)
    df = clean_data(df)
    print(f"Dossiers après nettoyage : {len(df)}")

    df = encode_features(df)
    X_train, X_test, y_train, y_test = prepare_datasets(df)
    print(f"Train : {len(X_train)} | Test : {len(X_test)}")

    # entraînement rapide pour valider le pipeline
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    acc = accuracy_score(y_test, model.predict(X_test))
    print(f"Accuracy du modèle de contrôle : {acc:.3f}")

    X_train.assign(defaut=y_train.values).to_csv("train.csv", index=False)
    X_test.assign(defaut=y_test.values).to_csv("test.csv", index=False)
    print("Jeux de données exportés : train.csv, test.csv")


if __name__ == "__main__":
    main()
