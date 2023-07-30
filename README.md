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



le code du fichier IA.py est compose de 3 parties :
1) Les imports des bibliothèques : openai et ConfigParser. 


2) Définition d'une collection de donnée et  des fonctions:

  - La collection de données est un dictionnaire contenant les choix de questions
  
  - Les fonctions sont les suivantes :
    
    #Une fonction qui  lit la clé API à partir d'un fichier de configuration  " Ai_config.cfg"
    def get_api_key(): 
        # Lecture du fichier de configuration
        # Récupération de la clé API à partir de la section 'openai'
        # Renvoi de la clé API
        
    
    # Cette fonction est un décorateur. Elle ne modifie pas le comportement de la fonction qu'elle décore.
    def IA(func):
    
    # La fonction chatGptAsk est décorée par la fonction IA. 
    @IA
    def chatGptAsk(question, selection):
        # Elle génère une question pour l'IA GPT-3.5-turbo 
        # renvoie sa réponse.
        
3) Configuration de la clé API pour la bibliothèque openai, en appelant la fonction get_api_key()
     
        
4) Affichage du menu et de la réponse via l'appel d'une fonction 

    # L'utilisateur choisit une question.
    # L'utilisateur entre le code à examiner.
    # La question et la sélection de l'utilisateur sont passées à la fonction chatGptAsk, et la réponse de l'IA est affichée.


