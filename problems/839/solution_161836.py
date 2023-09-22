from math import ceil
def carros (x, y):
    """calcula a quantidade de carros necessária, dado o número de pessoas"""
    return ceil (x//y)