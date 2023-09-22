from math import*
def carros (x,y=5):
    '''função que gera o número exato de carros que serão necessários para que x pessoas viagem,tendo em vista a capacidade y dos carros;int,int -> float'''
    return ceil(x/y)