# Documentation de la solution de Gestion de Projet

Ce projet vise à créer une solution de gestion de projets en utilisant Python et Django. Voici un aperçu des classes, fonctions et méthodes principales fonctionnelles pour répondre aux exigences en utilisant un service web.

...

## Implémentation

Pour implémenter ces fonctionnalités, nous avons créé les fichiers suivants :

**services.py**

Le fichier `services.py` contient la classe `ProjectService` avec les méthodes `insert_project_data` et `get_project_data` pour gérer les données du projet dans la base de données.

**ClientSender.py**

Le fichier `ClientSender.py` contient la classe `ClientSender` avec la méthode `send_project_data` pour envoyer les données du projet au service.

**ClientReceiver.py**

Le fichier `ClientReceiver.py` contient la classe `ClientReceiver` avec la méthode `receive_project_data` pour recevoir les données du projet à partir du service.

## Configuration de la Base de Données

Pour configurer la base de données avec Django, les commandes suivantes sont exécutées dans le terminal :

1. `python manage.py makemigrations finaleA15Service`: Cette commande génère des fichiers de migration en fonction des modèles de données.

2. `python manage.py migrate finaleA15Service`: Cette commande applique les migrations à la base de données, créant ainsi les tables nécessaires pour stocker vos données.

La mise á jour des modèles se fait dans le fichier `models.py` de l'application `finaleA15Service` avant de générer et d'appliquer les migrations.

...

Auteur : Kalilou Sy Savané
Date : 2023-10-02
