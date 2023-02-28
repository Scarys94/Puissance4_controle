#Puissance 4 - Jeu avec interface graphique Tkinter

#Description
Créé par Timothée RABOT, version 
Ce projet consiste en une implémentation du jeu de société Puissance 4, avec une interface graphique Tkinter permettant aux joueurs de jouer contre un adversaire humain. Les joueurs alternent pour placer des pions dans une grille de 6x7, le but étant d'aligner 4 pions horizontalement, verticalement ou en diagonale.

#Installation
Pour utiliser ce programme, vous devez avoir Python 3 installé sur votre ordinateur, ainsi que la bibliothèque Tkinter. Vous pouvez les installer en exécutant la commande suivante :

'''javascript
pip install tkinter
'''
Ensuite, vous pouvez cloner ce dépôt Git en exécutant la commande suivante :


git clone https://github.com/Scarys94/Puissance4_controle.git

#Utilisation
Pour lancer le jeu, exécutez le fichier _init_.py avec Python :


'''javascript
python _init_.py
'''
Vous pouvez alors jouer contre un autre joueur en cliquant sur les colonnes de la grille pour y placer vos pions.

#Stratégie de test unitaire
Dans ce projet, j'ai utilisé une stratégie de test unitaire pour m'assurer que les différentes fonctions du jeu fonctionnaient correctement. 
J'ai utilisé le module de pytest de Python pour écrire les tests unitaires. Les tests sont contenus dans le fichier test_puissance_4.py. J'ai écrit des tests pour les fonctions qui vérifient si un joueur a gagné la partie, si une colonne est pleine, et si un coup est valide.

Pour exécuter les tests unitaires, vous devez aller dans le fichier test puis vous pouvez exécuter la commande suivante :


'''javascript
pytest _init_.py
'''
Cela exécutera tous les tests dans le fichier test et affichera les résultats.

#Pourquoi tester unitairement avec pytest?
Les tests unitaires sont une approche importante pour assurer la qualité de votre code et éviter les erreurs. En testant chaque fonction de manière indépendante, vous pouvez vous assurer que chaque fonction est correcte et fonctionne comme prévu. Pytest est un outil de test unitaire populaire pour Python. Il est facile à utiliser et offre de nombreuses fonctionnalités pour tester votre code.

#Pourquoi utiliser une stratégie ascendante pour l'intégration?
Dans une stratégie ascendante, vous testez d'abord les parties les plus simples de votre application, puis vous ajoutez progressivement des couches de complexité. Cela vous permet de trouver des erreurs plus facilement et de vous assurer que chaque fonction est correcte avant de passer à la suivante. Cela permet également de détecter les erreurs plus tôt dans le processus de développement, ce qui peut vous faire gagner du temps à long terme. En utilisant cette approche, vous pouvez vous assurer que chaque fonction est testée de manière approfondie avant de passer à l'intégration avec les autres parties de l'application.

En utilisant cette stratégie de test unitaire, je peux m'assurer que le jeu fonctionne correctement même lorsque je fais des modifications dans le code. Cela me permet de détecter rapidement les erreurs et de les corriger avant qu'elles ne causent des problèmes pour les utilisateurs du jeu
