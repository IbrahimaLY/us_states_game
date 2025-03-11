# U.S. States Game

Ce projet est un jeu interactif pour apprendre et tester vos connaissances sur les 50 États des États-Unis. Le jeu utilise une carte des États-Unis et vous demande de deviner le nom des États un par un. Si vous réussissez à deviner tous les États, vous gagnez !

## Fonctionnalités

- **Interface graphique** : Utilise la bibliothèque `turtle` pour afficher une carte des États-Unis.
- **Gestion des données** : Les noms et les coordonnées des États sont stockés dans un fichier CSV (`50_states.csv`).
- **Sauvegarde des progrès** : Si vous quittez le jeu avant de deviner tous les États, les États non devinés sont enregistrés dans un fichier `states_to_learn.csv`.

## Fichiers inclus

- **`50_states.csv`** : Contient les noms des États et leurs coordonnées (x, y) sur la carte.
- **`blank_states_img.gif`** : Une image de la carte des États-Unis utilisée comme fond pour le jeu.
- **`main.py`** : Le script principal du jeu.
- **`states_to_learn.csv`** : Fichier généré contenant les États non devinés.

## Comment jouer

1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir Python installé.
3. Installez les dépendances nécessaires :
   ```bash
   pip install pandas
   ```
4. Exécutez le script **main.py** :
    ```bash
    python main.py 
   ```
5. Devinez les noms des États en les saisissant dans la boîte de dialogue.
6. Si vous souhaitez quitter avant la fin, tapez "Exit". Les États non devinés seront enregistrés dans **states_to_learn.csv**.