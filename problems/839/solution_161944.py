from math import ceil
def carros (pessoas,capacidade=5):
    """int, int -> int"""
    return round((pessoas/capacidade)+0.5)