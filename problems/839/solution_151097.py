import math
def carros (p: int, c: int =5)-> int:
    """calcula quantos carros são necessários para a viagem, dado o número de
    pessoas p e a capacidade dos carros c"""
    return math.ceil (p/c)