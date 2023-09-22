import math
def conta_frases(texto):
    """Função que conta o número de frases de um determinado texto
       parâmetro de entrada:str
       parâmetro de saída:int"""
    return str.count('...')+str.replace('...','.')+str.count('.')+str.count('!')+str.count('?')