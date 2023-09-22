from math import floor
def bolos (a,b,c):
    '''retorna a quantidade de bolos possivel de ser feita dadas as quantidades de cada ingrediente (farinha-a; b-ovos; c-leite)'''
    return min(floor(a/2),floor(b/3),floor(c/5))