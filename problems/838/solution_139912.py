from math import floor
def num_bombons(d, p):
    """Pedrinho deseja comprar bombons. Com uma quantia d em dinheiro,
    e sendo o preço de cada bombom p, calcula quantos bombons Pedrinho é
    capaz de comprar"""
    return floor(d/p)