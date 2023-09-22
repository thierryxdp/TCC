from math import round
def carros(pessoas, capacidade=5):
    """calcula o numero de carros necessarios para uma viagem dados o numero de pessoas e a capacidade dos carros, 
    caso nao seja definida a capacidade e igual a 5"""
    return round(pessoas/capacidade)