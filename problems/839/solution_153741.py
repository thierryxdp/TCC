from math import ceil
def carros(p,c=5):
    '''Função que determina o número de carros
    que podem ser utilizados, sabendo o número 
    de pessoas que vão na viagem'''
    return ceil(p/c)