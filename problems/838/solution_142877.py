from math import floor

def num_bombons (s,p):
    '''funcao que retorna a quantidade de bombons de preco unitario p
    que podera ser adquirida com um determinado saldo s
    float,float -> int'''
    return floor(s/p)