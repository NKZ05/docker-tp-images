# Exercice 1 - Première image Flask

Objectif: dockeriser une application Flask simple et versionner l'image avec des tags.

## Contexte

L'application expose une page HTTP sur le port `5000` et renvoie:
- `Hello Docker!`
- `Mon premier conteneur Flask`

## Fichiers du projet

- `app.py`
- `requirements.txt`

## Travail a faire

1. Creer un `Dockerfile` qui:
- utilise `python:3.12-slim`
- copie les fichiers necessaires
- installe les dependances
- expose le port `5000`
- lance l'application avec `python app.py`

2. Creer un `.dockerignore` pour exclure:
- `__pycache__/`
- `*.pyc`
- `.git/`

3. Construire l'image avec le tag `hello-flask:1.0.0`.
4. Lancer le conteneur et verifier que l'application repond sur `http://localhost:5000`.
5. Creer le tag `hello-flask:latest` et verifier la presence des deux tags.

Les commandes doivent etre fournies dans un fichier separe `COMMANDS.md`.

## Critères de validation

- Dockerfile propre et court (moins de 10 lignes idealement)
- Build sans erreur
- Application accessible sur `http://localhost:5000`
- Deux tags presents: `1.0.0` et `latest`
