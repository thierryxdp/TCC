import math

def carros (passageiros, assentos=5):
    """calcula a quantidade de carros mínima dado a 
    quantidade de passageiros e assentos dos carros. """
    return math. ceil (passageiros/assentos)