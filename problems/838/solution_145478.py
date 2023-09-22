import math
def num_bombons (d,p):
    '''função calcula a quantidade de bombons que podem ser comprados dados
    o dinheiro (d) que a pessoa possui e o preço (p) da unidade de bombom'''
    return math.floor(d/p)