from math import ceil
def carros(p,c=5):
    """Calcular o número exato de carros necessários para 
    esta viagem, dado o número de entrada"""
    return ceil(p/c)