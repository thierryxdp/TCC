from math import floor
def num_bombons(dinheiro, preco):
    '''funcao que calcula quantos bombons
    podem ser comprados com determinada quantia
    em dinheiro'''
    return floor(dinheiro/preco)