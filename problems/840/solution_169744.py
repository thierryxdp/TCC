from math import*
def bolos (a,b,c):
    '''função que gera a quantidade de bolos tendo em vista a quantidade (a) de xícaras de farinha de trigo,(b) de ovos e (c) de de colhere de sopa de leite; int,int,int ->int'''
    return min(floor(a/2),floor(b/3),floor(c/5))