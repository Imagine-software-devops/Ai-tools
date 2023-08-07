# Ai-tools
Ai tools using chatgpt 4 api key

Ai tools using chatgpt 3 api key

C'est une première version d'un module réalisé dans le cadre d'une démarche Devops lors de la formation M2I-Marseille2023

Ce module permet à l'utilisateur de sélectionner l'un des 3 choix suivants :
1 : Corriger un code
2 : Optimiser un code
3 : Commenter un code


Il utilise la bibliothèque OpenAI pour questionner l'IA GPT-3.5-turbo.
Dans un premier temps, l'utilisateur choisit l'une des 3 options, puis il introduit son code.
A la suite, le module renvoie la réponse de l'IA.



Prérequis 
Avant d'utiliser le module :
1) Dans votre compte OpenAI, récupérer votre clé d'API à l'adresse https://platform.openai.com/account/api-keys.

2) Installer la bibliothèque openai avec la commande suivante dans un shell:
    pip install openai   (shell ubuntu)


Structure du module
Le module est organisé de la manière suivante :
IA.md                    # le présent fichier d'explication
IA.py                    # le code en python
Config/                  # dossier config   
    Ai_config.cfg        # le fichier config qui contient la clé API OpenAi



