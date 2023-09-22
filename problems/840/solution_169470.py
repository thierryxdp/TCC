import math

def bolos (A,B,C):
    '''função que recebe a quantidade de xícaras, ovos e
    colheres de leite e retorna a quantidade de bolos int, int=int'''
    return min (A//2,B//3,C//5)