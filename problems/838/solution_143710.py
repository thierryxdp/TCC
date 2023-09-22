from math import floor

def num_bombons (d,pb):
    '''Dado um determinado valor em dinheiro e o preço do bombom
    calcule o menor número inteiro de bombons que pode ser comprado'''
    return floor (d/pb)