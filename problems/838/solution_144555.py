import math

def num_bombons (dinheiro, preco_bombom):
    '''esta funcao calcula quantos bombons pode-se obter, tendo o dinheiro e o preco de cada bombom'''
    return math.floor (dinheiro / preco_bombom)