from math import ceil
def bolos (A=2,B=3,C=5):
    '''função que define a quantidade exata de bolos
    que João deverá fazer com A xícaras de farinha,
    B ovos e C colheres de sopa de leite'''
    return ceil(A/2) + ceil(B/3) + ceil(C/5)