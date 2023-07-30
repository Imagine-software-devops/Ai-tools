usr/bin/env python
# importer des bibiliothèques 
import openai
from configparser import ConfigParser

def create_config(keyapi):
  """
  Creates a configuration file with the provided API key.

  Parameters:
      keyapi (str): The API key to be stored in the configuration file.
  """
  config = ConfigParser()  
  config["openai"]={
    "api_key" : f"{keyapi}", 
  }
  with open(r"AI_config.cfg", 'w') as f:
    config.write(f)
    print("Le fichier de configuration a été créé avec succès")


def get_api_key():
  """
  Reads the API key from the configuration file and returns it.
openai.api_key =
  Returns:
    str: The API key read from the configuration file.
  """
  config = ConfigParser()
  config.read('config/AI_config.cfg')

  API_KEY = config.get('openai', 'api_key')
  return API_KEY

#Récuperation de la clé
openai.api_key=get_api_key()

# Un dictionnaire contenant les choix de questions
Choix = {
    "1" : "Corrige moi le code suivant sans explication",
    "2" : "Optimise moi le code suivant sans explication",
    "3" : "Commente moi le code suivant sans explication"
}

def IA(func):    
    """
    Decorator function that wraps another function `func` and returns a new function `inner1`.
    The `inner1` function takes two parameters: `question` (question to be passed to `func`) and `selsection` (selsection to be passed to `func`).
    The `inner1` function calls the `func` function with the given parameters and stores the returned value in `returned_value`.
    Finally, the `inner1` function returns the `returned_value` to the original frame.

    Parameters:
    - `func` : function
        The function to be wrapped.

    Returns:
    - `inner1` : function
        The wrapped function.
    """
    def inner1(question, selsection):  
        # getting the returned value
        returned_value = func(question, selsection)
        # returning the value to the original frame
        return returned_value
    return inner1

# une fonction qui interroge l'API GhatGpt
@IA
def chatGptAsk(question, selection):
    """
    Generates a question to ask the chatbot using OpenAI's GPT-3.5-turbo model.
    
    Args:
        question (str): The question to ask the chatbot.
        selection (int): The index of the choice from the 'Choix' list to include in the chat.
    
    Returns:
        str: The response from the chatbot, obtained using the GPT-3.5-turbo model.
    """
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": Choix[str(selection)]},
        {"role": "user", "content": question}
      ]
    )
    return response.choices[0].message.content + "\n"
'''
# L'utilisateur choisit une question.
selection= input("selection entre : \n \
                1 : Corrige moi le code, suivant sans explication\n \
                2 : Optimise moi le code suivant sans explication \n \
                3 : Commente moi le code suivant sans explication \n")

# L'utilisateur entre le code à examiner.
question = input("Entrez votre code :")

# La question et la sélection de l'utilisateur sont passées à la fonction chatGptAsk, et la réponse de l'IA est affichée.
print("asking:", chatGptAsk(question, selection))

'''

def main():
    keyapi = input("Entrez votre API key : \n")
    create_config(keyapi)
    openai.api_key = get_api_key()
    
    
    while True:
        selection= int(input("selection entre : \n \
                  1 : Corrige moi le code suivant sans explication, \n \
                  2 : Optimise moi le code suivant sans explication \n \
                  3 : Commente moi le code suivant sans explication \n \
                  4 :  Quiter le programme \n "))
        print(type(selection))
        if selection == 4:
          print("Au revoir")
          return 
          
        question = input("Entrez votre code : \n")
        print(chatGptAsk(question, selection))


if __name__ == "__main__":
    
    main()
