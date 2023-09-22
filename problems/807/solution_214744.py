import re
def conta_frases(frase):
    """ Função que conta a quantidade de frases em um texto """
    a = frase
    n = len(re.split("[ . ! ... ]", a))
    return n