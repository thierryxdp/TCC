from math import floor
def num_bombons(x,y):
    """função que define quantos bombons uma pessoa pode comprar sendo y o valor de um bombom e x o dinheiro disponivel da pesso"""
    return floor(x/y)