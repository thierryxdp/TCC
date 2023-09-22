from math import ceil
def carros(p,l=5):
    """retorna o numero de carros necessarios para viagem em função da capacidade l e do numero de pessoas p"""
    return ceil(p/l)