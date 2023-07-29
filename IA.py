#!/usr/bin/env python
import openai
from configparser import ConfigParser
def get_api_key():
  """
  Reads the API key from the configuration file and returns it.

  Returns:
    str: The API key read from the configuration file.
  """
  config = ConfigParser()
  config.read('config/AI_config.cfg')

  API_KEY = config.get('openai', 'api_key')
  return API_KEY

openai.api_key = get_api_key()

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
        {"role": "system", "content": Choix[selection]},
        {"role": "user", "content": question}
      ]
    )
    return response.choices[0].message.content + "\n"

selection= input("selection entre : \n \
                1 : Corrige moi le code suivant sans explication, \n \
                2 : Optimise moi le code suivant sans explication \n \
                3 : Commente moi le code suivant sans explication \n")
question = input("Entrez votre code :")

print("asking:", chatGptAsk(question, selection))


