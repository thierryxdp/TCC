from math import floor
def bolos(A,B,C):
    '''Calcula a quantidade de bolo que se pode fazer dado:
    xicaras de farinha: A.
    ovos:B.
    Colheres de sopa de leite:C'''
    return floor(min((A/2),(B/3),(C/5)))