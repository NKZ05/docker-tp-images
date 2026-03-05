# TP Docker - Gestion des images

Le but est de vous faire pratiquer, pas a pas, la creation, l'optimisation, le versionnage et la publication d'images.

## Objectifs pedagogiques

A la fin du TP, vous devez etre capable de:
- ecrire un Dockerfile fonctionnel
- utiliser un `.dockerignore`
- optimiser un build Docker (ordre des instructions, image de base)
- gerer des tags (`1.0.0`, `latest`, etc.)
- publier une image sur Docker Hub
- comprendre l'interet d'un build multistage

## Organisation du TP

Le TP est compose de 3 exercices progressifs:

1. `exercice-1-flask`
- Premiere image Docker pour une application Flask
- Focus: Dockerfile de base, tags, verification locale

2. `exercice-2-weather-api`
- API Node.js a optimiser et publier
- Focus: cache de build, image legere, publication Docker Hub

3. `exercice-3-stats-api`
- Application Python en plusieurs versions
- Focus: multistage build, versionnement avance, gestion de `latest`

## Ce que vous devez rendre

Dans chaque dossier d'exercice, vous devez fournir:
- `README.md` (consigne / contexte / criteres, sans commandes)
- `Dockerfile`
- `COMMANDS.md` (toutes les commandes executees pour realiser l'exercice)

Le format attendu est precise dans [CONTRIBUTING.md](./CONTRIBUTING.md).

## Methode de travail conseillee

- Lire d'abord la consigne de l'exercice.
- Produire un Dockerfile minimal qui fonctionne.
- Tester localement avant toute optimisation.
- Optimiser ensuite (taille, couches, cache).
- Documenter vos commandes dans `COMMANDS.md`.

## Evaluation

Vous serez evalues sur:
- la conformite a la consigne
- la qualite du Dockerfile
- la capacite a produire une image qui fonctionne
- la qualite du versionnage et de la publication
- la clarte du rendu

Bon TP.
