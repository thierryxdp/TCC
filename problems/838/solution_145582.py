from math import floor
def num_bombons (D,P):
    '''retorna a quantidade de bombons possivel de ser comprada dados o dinheiro(D) e o preco(P) de cada bombom'''
    return floor(D/P)