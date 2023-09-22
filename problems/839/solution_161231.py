from math import*
def carros(p,c=5):
    """Dado um número de pessoas p, calcula quantos veículos de capacidade c são necessários para tranportá-los"""
    return ceil(p/c)