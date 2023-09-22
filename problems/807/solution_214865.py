import math
def conta_frases('frase'):
    """Função que conta o número de frases de um determinado texto
       parâmetro de entrada:str
       parâmetro de saída:int"""
    return str.count('frase','.')+ str.count('frase','!')+ str.count('frase','?') + str.count('frase','...')