import math
def bolos (a,b,c):
    '''Função que dado quantidades de xícaras de farinha de trigo a, ovos b e colheres de sopa c;
    retorna possibilidades da realização de uma receita de bolo;
    int, int, int -> int'''
    return math.ceil(a/2,b/3,c/5)