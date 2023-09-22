from math import*

def bolos ( farinha, ovos, leite):
    '''Calcula o número de bolos que podem ser feitos com determinada
    quantidade  de xícaras de farinha de trigo, de ovos e de colheres de 
    sopa de leite
    int,int -> int'''
    return floor(min((farinha / 2),(ovos / 3), (leite / 5)))