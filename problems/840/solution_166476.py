from math import floor
def bolos (A,B,C):
    """ Função que ajuda João a definir quantos bolos serão feitos de acordo com os ingredientes que tem
    A = xícaras de farinha de trigo
    B = ovos
    C = colheres de sopa de leite"""
    return floor (min (A/2, B/3, C/5)