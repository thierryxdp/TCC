def carros(p,c=5):
    '''função retorna a quantidade de carros com capacidade "c" necessarios para levar uma quantidade "p" de pessoas em uma viagem
    int, int -> int'''
    return ceil(p//c)