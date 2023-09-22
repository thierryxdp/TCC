import math
def carros(gente, espaco=5):
    """Calcula e retorna a quantidade de carros necessários
       para levar a quantidade de pessoas fornecidas"""
    return math.ceil(gente/espaco)