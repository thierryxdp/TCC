import math 
def bolos(A,B,C): 
    ''' Retorna a quantidade maxima de bolos que Joao consegue fazer, dadas
    como entrada as quantidades de xícaras de farinha (A), de ovos (B) e de
    colheres de sopa de leite (C) que ele possui, considerando a realizacao 
    apenas de receitas inteiras;
    int, int, int -> int'''
    return min(math.floor(A/2), math.floor(B/3), math.floor(C/5))