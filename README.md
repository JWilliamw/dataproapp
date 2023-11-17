# dataproapp
Solution web de visualisation de données

Nous utilisons ici PostgreSQL pour stocker les données. 

## Data prep
Nous avons un dossier data prep dans lequel se trouve un script de préparation et d'ingestion des données dans la base de données. Afin d'éviter de partager le mot de passe sur github, nous l'avons remplacer par des données fake. IL suffira justre de créer une base de données dans POSTGRESQL et mettre les enfants pour pouvoir executer le script. Voir fichier .env.example


## Requirements
Le fichier requirement contient les librairies nécessaires pour tester le site; On pourra les installer avec : pip install -r requirements

## APP
Le corps de notre site se trouve dans le dossier APP avec les templates html, css, le modèle de données ainsi que les routes. 