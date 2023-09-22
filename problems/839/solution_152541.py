from math import *
def carros(pessoas,capacidade=5):
    """retorna o número de carros com capacidade determinada necessários para transportar um número determinado de pessoas (se a capacidade não forespecificada, será usada a capacidade padrão de 5 pessoas)"""
    return ceil(pessoas/capacidade)