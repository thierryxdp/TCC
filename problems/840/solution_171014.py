import math
def bolos (A,B,C):
    '''função calcula a quantidade máxima de bolos que podem ser feitos,
    informando respectivamente o número de xícaras de farinhas de trigo (A,
    o número de ovos (B) e o número de colheres de sopa de leite (C) que se
    possui'''
    return min ((math.floor(A/2)),(math.floor(B/3)),(math.floor(C/5)))