from math import floor
def bolos (A,B,C):
    '''função que define a quantidade exata de bolos
    que João deverá fazer com A xícaras de farinha,
    B ovos e C colheres de sopa de leite'''
    return floor((2*A+3*B+5*C)/10)